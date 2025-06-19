from os import environ
from apscheduler.schedulers.background import BackgroundScheduler

#? telebot
from telebot import TeleBot
from telebot.types import Message, BotCommand
from telebot.custom_filters import StateFilter, IsDigitFilter, TextMatchFilter
from telebot.states.sync.middleware import StateMiddleware

#? engine
from bot_engine.data.Users import *


#? modules
from bots.sport_home_bot.bot.Filters import SimpleAccessLevelFilter
from bots.sport_home_bot.bot.helpers import Helpers
from bots.sport_home_bot.parser.zelart_parser import PrestaShopScraper
from bots.sport_home_bot.database.mongodb import Database
from bots.sport_home_bot.bot.exception_handler import ExceptionHandler

#? data
from bots.sport_home_bot.bot.messages import messages
from bots.sport_home_bot.bot.Commands import bot_commands
from bots.sport_home_bot.bot.constant_variables import constant_variables


class Handlers:
    def __init__(self, bot: TeleBot, database: Database, helpers: Helpers, scheduler: BackgroundScheduler):
        self.bot = bot
        self.db = database
        self.helpers = helpers
        self.messages = messages

        self.scheduler = scheduler

        self.access_levels = [AccessLevel.USER, AccessLevel.ADMIN, AccessLevel.SUPER_ADMIN]


    def setup_command_handlers(self):
        self._setup_start_handler()
        self._add_product_command_chain()
        self._set_time_command_chain()
        self._remove_product_command_chain()
        self._setup_parse_handler()
        self._setup_info_handler()
        self._setup_menu_handler()


    def _setup_start_handler(self):
        @self.bot.message_handler(commands=[bot_commands.start.name], access_level=self.access_levels)
        def send_welcome(message: Message):
            """ creates user with USER access_level """
            user = {
                "chat_id": message.from_user.id,
                "username": message.from_user.username,
                "access_level": AccessLevel.USER
            }

            self.db.insert_user(user)

            self.bot.send_message(message.from_user.id, self.messages.start.format(constant_variables["ZELART_WEBSITE"]))
            self.helpers.get_info(message)


    def _add_product_command_chain(self):
        access_levels = [AccessLevel.USER, AccessLevel.ADMIN, AccessLevel.SUPER_ADMIN]
        @self.bot.message_handler(commands=[bot_commands.add_product.name], access_level=self.access_levels) 
        def add_product(message: Message):
            """ first step of adding product """
            self.bot.send_message(message.from_user.id, self.messages.add_product_first_step.format(constant_variables["ZELART_WEBSITE"]))
            self.bot.register_next_step_handler(message, process_parse_link)

        def process_parse_link(message: Message):
            """ second step of adding product """
            try:
                link = message.text
                parser = PrestaShopScraper()
                product = parser.scrape_product(link)

                if isinstance(product, str):
                    self.bot.send_message(message.from_user.id, messages.product_not_found)
                    return

                self.db.insert_product(product)

                if product["isHidden"] == True:
                    stock = "Немає в наявності"
                elif product["isHidden"] == False:
                    stock = "Є в наявності"

                discount_string = ""
                if product["priceCur"] != product["priceWithDiscount"]:
                    discount_string = self.messages.optional_discount_string.format(product["priceWithDiscount"])
                
                self.bot.send_message(message.from_user.id, self.messages.add_product_second_step.format(link, product["title"], product["priceCur"], discount_string, product["priceSrp"], stock))

            except:
                self.bot.send_message(message.from_user.id, self.messages.add_product_second_step_fail)


    def _set_time_command_chain(self):
        access_levels = [AccessLevel.USER, AccessLevel.ADMIN, AccessLevel.SUPER_ADMIN]
        @self.bot.message_handler(commands=[bot_commands.set_time.name], access_level=self.access_levels)
        def set_time(message: Message):
            """ first step of setting time """
            parse_time = self.helpers.get_parse_time()
            
            self.bot.send_message(message.from_user.id, self.messages.set_time_first_step.format(parse_time))
            self.bot.register_next_step_handler(message, set_time_second_step)

        def set_time_second_step(message: Message) -> None:
            """ sets check time from given message """
            time: str = message.text
            hour, minutes = self.helpers.convert_time(time)
            #? print("🐍 hour / minutes: ",hour, minutes)
            self.helpers.save_time([hour, minutes])

            if hour is None or minutes is None:
                self.bot.send_message(message.chat.id, self.messages.set_time_second_step_fail)
            else: 
                self.helpers.schedule_parse_time(hour, minutes)
                minutes = self.helpers.format_minutes(minutes)

                self.bot.send_message(message.chat.id, self.messages.set_time_second_step_success.format(hour, minutes))


    def _remove_product_command_chain(self):
        @self.bot.message_handler(commands=[bot_commands.remove_product.name], access_level=self.access_levels)
        def remove_product(message: Message):
            """ first step of removing product """
            self.bot.send_message(message.from_user.id, self.messages.remove_product_first_step)
            self.bot.register_next_step_handler(message, remove_product_second_step)

        def remove_product_second_step(message: Message):
            """ second step of removing product """
            link = message.text
            parser = PrestaShopScraper()
            product = parser.scrape_product(link)
            #? print("🐍 product: ",product)

            if product:
                product_id = product["id"]
                self.db.remove_product(product_id)
                self.bot.send_message(message.chat.id, self.messages.remove_product_second_step_success.format(product_id))

            else:
                print(f"Can't get product info by this link: {link}")
                self.bot.send_message(message.chat.id, self.messages.remove_product_second_step_fail)


    def _setup_parse_handler(self):
        @self.bot.message_handler(commands=[bot_commands.parse.name], access_level=self.access_levels)
        def parse(message: Message):
            self.helpers.update_products_daily()


    def _setup_info_handler(self):
        @self.bot.message_handler(commands=[bot_commands.info.name], access_level=self.access_levels)
        def get_info(message: Message):
            self.bot.send_message(message.from_user.id, self.messages.info)
            self.helpers.get_info(message)


    def _setup_menu_handler(self):
        @self.bot.message_handler(commands=[bot_commands.menu.name], access_level=self.access_levels)
        def get_help(message: Message):
            self.bot.send_message(message.from_user.id, self.messages.help)