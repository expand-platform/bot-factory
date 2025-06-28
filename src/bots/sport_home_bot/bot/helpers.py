from os import environ
from time import sleep

from apscheduler.schedulers.background import BackgroundScheduler

from telebot import TeleBot
from telebot.types import Message

from bots.sport_home_bot.database.mongodb import Database, DB_COLLECTIONS, STATS_DOCUMENT
from bots.sport_home_bot.bot.messages import messages
from bots.sport_home_bot.parser.zelart_parser import PrestaShopScraper
from bots.sport_home_bot.bot.dataclass import FIELDS

from data.constants import ENVIRONMENT

SLEEP_TIME = 1.2  


class Helpers:
    def __init__(self, bot: TeleBot, database: Database, scheduler: BackgroundScheduler):
        self.ENVIRONMENT: str = environ["ENVIRONMENT"]
        self.db = database
        self.bot = bot
        self.scheduler = scheduler

    
    #! убрать костыль с юзерами
    def notify_users(self, message: str) -> None:
        users = self.db.get_users()

        for user in users:
            try: 
                self.bot.send_message(user["chat_id"], message)
                sleep(SLEEP_TIME)
            except Exception as e:
                print(f"Error sending message to user {user['chat_id']}: {e}")

 
    def update_products_daily(self):
        """ updates products in DB and sends message to users """
        self.notify_users(messages.scheduler_start_parsing)
        
        products = self.db.get_products()  
        parser = PrestaShopScraper()
        parser.login()

        all_products_change_status = False
        
        for product_from_database in products:
            link = product_from_database["url"]
            product_from_parser = parser.parse_product(link)
            #? print("🐍 link:", link)

            #? when product is no longer exists on the website,
            #? remove it from db
            if isinstance(product_from_parser, str):
                self._handle_removed_product(link)
                all_products_change_status = True
                continue

            product_change_status = self._handle_product_change(product_from_database, product_from_parser, link)
            if product_change_status:
                all_products_change_status = True

        self._notify_final_status(all_products_change_status)


    def _handle_removed_product(self, link: str) -> None:
        removed_product = self.db.find(key="url", value=link)
        
        if removed_product:
            self.db.remove_product(id=removed_product["id"])
        
        self.notify_users(messages.product_was_removed.format(link))


    def _handle_product_change(self, product_from_database, product_from_parser, link: str) -> bool:
        product_change_status = False
        reply_string = messages.scheduler_parse_string_start.format(product_from_parser["title"], link)
        
        for product_key in product_from_parser:
            if product_key in ("priceCur", "priceWithDiscount", "priceSrp", "isHidden"):
                if product_from_parser[product_key] != product_from_database[product_key]:
                    print("change happened")
                    product_change_status = True

                    field = FIELDS.get(product_key)

                    if not field:
                        continue

                    key = field.display_name
                    key_value_database = field.format_func(product_from_database[product_key])
                    key_value_parser = field.format_func(product_from_parser[product_key])

                    if field.unit and product_key != "isHidden":
                        key_value_database += f" {field.unit}"
                        key_value_parser += f" {field.unit}"


                    reply_string += messages.scheduler_parse_string_add.format(key, key_value_database, key_value_parser)
                    self.db.update("url", link, product_key, product_from_parser[product_key])

        
        if product_change_status:
            print(f"➕ product has changed")
            self.increase_products_tracked()
            self.notify_users(reply_string)
        else:
            print(f"➖ product has not changed")
        
        return product_change_status


    def increase_products_tracked(self) -> None:
        products_tracked = self.db.get_products_tracked_stats()
        self.db.update_one_document(collection_name=DB_COLLECTIONS.stats, key=STATS_DOCUMENT.products_tracked, value=products_tracked+1)


    def _notify_final_status(self, all_products_change_status: bool) -> None:
        if not all_products_change_status:
            self.notify_users(messages.scheduler_parse_string_no_changes)
        else:
            self.notify_users(messages.parse_final)

        
    def schedule_parse_time(self, hour: int = 19, minute: int = 0) -> None:
        self.scheduler.remove_all_jobs()

        #? on server we substract 3 hours
        if self.ENVIRONMENT == ENVIRONMENT.production:
            if hour >= 3:
                hour -= 3
            else:
                #? We can't make hours negative, so we transform it like these:
                #? -1 = 23
                #? -2 = 22
                #? -3 = 21
                hour = 24 + (hour - 3)
            self.scheduler.add_job(self.update_products_daily, 'cron', hour=hour, minute=minute) 

        else:
            self.scheduler.add_job(self.update_products_daily, 'cron', hour=hour, minute=minute) 
        
        #? print(scheduler.get_jobs())
        print(f"🟢 Products check will be started at {hour}:{minute}")


    def save_time(self, time: list[int]):
        """ saves time to DB """
        self.db.update_one_document(key="parse_time", value=time)


    def format_minutes(self, minutes: int) -> str:
        """Formats minutes as a 2-digit string (e.g. 0 → '00', 5 → '05')"""
        return f"{minutes:02}"


    def convert_time(self, time: str = "") -> list[int] | list[None]:
        """ converts string into list of integers """
        if ":" in time:
            return list(map(int, time.split(":")))
        return [None, None] 


    def get_parse_time(self) -> str:
        hours, minutes = self.db.get_parse_time()
        minutes = self.format_minutes(minutes)
        return f"{hours}:{minutes}"
    
    def count_cost_of_work(self) -> int:
        COST_OF_WORK = 100 # uah
        products_tracked = self.db.get_products_tracked_stats()
        hours_of_work = products_tracked // 2
        return hours_of_work * COST_OF_WORK
    

    def get_info(self, message: Message):
        products_count = self.db.get_products_count()
        parse_time = self.get_parse_time()
        products_tracked = self.db.get_products_tracked_stats()
        
        cost_of_work = self.count_cost_of_work()
        
        info_message = messages.info_string.format(products_count, parse_time, products_tracked, cost_of_work)

        self.bot.send_message(message.chat.id, info_message, parse_mode="Markdown")
