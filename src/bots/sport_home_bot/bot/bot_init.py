from bots.sport_home_bot.bot.Handlers import Handlers
from bots.sport_home_bot.bot.Bot import Bot
from dotenv import load_dotenv
from os import environ

from apscheduler.schedulers.background import BackgroundScheduler

from bots.sport_home_bot.bot.helpers import Helpers
from bots.sport_home_bot.database.mongodb import Database
from data.constants import ENVIRONMENT


def start_bot():
    """ initializes core modules """
    print(f"✅ Bot launched!") 
    load_dotenv()
    environment = environ["ENVIRONMENT"]

    db = Database()
    bot = Bot(db)

    #? scheduler
    scheduler = BackgroundScheduler()
    hour, minute = db.get_parse_time()
    scheduler.start()

    #? helpers
    helpers = Helpers(bot=bot._bot, database=db, scheduler=scheduler)
    helpers.schedule_parse_time(hour=hour, minute=minute) 

    #? handlers
    handlers = Handlers(bot=bot._bot, database=db, helpers=helpers, scheduler=scheduler)
    handlers.setup_command_handlers()

    #? start bot
    if environment == ENVIRONMENT.development:
        print("⚙️  Bot is running in development mode")
        bot._bot.infinity_polling(restart_on_change=True)
    
    elif environment == ENVIRONMENT.production:
        print("🌐  Bot is running in production mode")
        bot._bot.infinity_polling()

    else:
        raise Exception("❌ Set ENVIRONMENT in .env file!")
