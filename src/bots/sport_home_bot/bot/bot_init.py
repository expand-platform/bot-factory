from bots.sport_home_bot.bot.bot_handlers import Bot
from dotenv import load_dotenv
from os import environ

from data.constants import ENVIRONMENT


def start_bot():
    print(f"✅ Bot launched!") 
    environment = environ["ENVIRONMENT"]

    if environment == ENVIRONMENT.development:
        print("⚙️  Bot is running in development mode")
        Bot().bot.infinity_polling(restart_on_change=True)
    
    elif environment == ENVIRONMENT.production:
        print("🌐  Bot is running in production mode")
        Bot().bot.infinity_polling()

    else:
        raise Exception("❌ Set ENVIRONMENT in .env file!")
