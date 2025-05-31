#? configs
from api.api_clients import API_CLIENTS
from bots.trading_bot.config.langConfig import DEFAULT_LANGUAGE
from bots.trading_bot.config.env import DATABASE_TOKEN, SUPER_ADMIN_ID, ADMIN_IDS, BINANCE_TOKEN, BINANCE_SECRET
from bots.trading_bot.config.dbConfig import DATABASE_NAME
from bots.trading_bot.config.langConfig import DEFAULT_LANGUAGE

#? bot engine
from bot_engine.bot.Bot import Bot
from bot_engine.languages.Languages import Languages
from bot_engine.database.Database import Database

#? engine customization
from bots.trading_bot.bot.BotPlugins import MyBotPlugins
from bots.trading_bot.server.Server import TradingBotServer

#? languages
from bots.trading_bot.locales.uk import UK_LOCALE
from bots.trading_bot.locales.ru import RU_LOCALE
  
#? dialogs
from bots.trading_bot.handlers.BotHandlers import BotHandlers
from bots.trading_bot.handlers.CommonHandlers import CommonHandlers
from bots.trading_bot.handlers.UserHandlers import UserHandlers
from bots.trading_bot.handlers.AdminHandlers import AdminHandlers

#? bot-specific settings (API etc)
from api.BinanceAPI import BinanceAPI

#? generic components
languages = Languages(active_lang=DEFAULT_LANGUAGE)

#? core parts
db = Database(DATABASE_TOKEN, DATABASE_NAME, SUPER_ADMIN_ID, ADMIN_IDS)
binance_api = BinanceAPI(TOKEN=BINANCE_TOKEN, SECRET=BINANCE_SECRET)
bot = Bot(db, languages)


#? bot settings
bot_plugins = MyBotPlugins(languages=languages, db=db, bot=bot)

#? bot settings
bot_plugins.set_languages(locales=[UK_LOCALE, RU_LOCALE], bot_language=DEFAULT_LANGUAGE)
bot_plugins.set_database()

#? Slash commands and user dialogs
bot_plugins.set_menu_commands()

#? bot handlers
bot_handlers = BotHandlers(db, languages, bot)
bot_handlers.add_api_client(client_name=API_CLIENTS.Binance, client_api=binance_api)

common_handlers = CommonHandlers(db, languages, bot)
user_handlers = UserHandlers(db, languages, bot)
admin_handlers = AdminHandlers(db, languages, bot)

#? set handler 
bot_plugins.set_handlers(common_handlers)
bot_plugins.set_handlers(user_handlers)
bot_plugins.set_handlers(admin_handlers)

#? run server with bot
server = TradingBotServer(bot=bot)
server.run()
