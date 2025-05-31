# ? configs
from bots.platform_bot.config.langConfig import DEFAULT_LANGUAGE
from config.env import DATABASE_TOKEN, SUPER_ADMIN_ID, ADMIN_IDS
from bots.platform_bot.config.dbConfig import DATABASE_NAME
from bots.platform_bot.config.langConfig import DEFAULT_LANGUAGE

# ? bot engine
from bot_engine.bot.Bot import Bot
from bot_engine.languages.Languages import Languages
from bot_engine.database.Database import Database

# ? engine customization
from bots.platform_bot.plugins.BotPlugins import MyBotPlugins
from bots.platform_bot.server.BotServer import BotServer

# ? languages
from bots.platform_bot.locales.uk import UK_LOCALE
from bots.platform_bot.locales.ru import RU_LOCALE 

#? plugins
from bots.platform_bot.handlers.BotHandlers import BotHandlers
from bots.platform_bot.handlers.UserHandlers import UserHandlers
from bots.platform_bot.handlers.AdminHandlers import AdminHandlers
from bots.platform_bot.handlers.CommonHandlers import CommonHandlers


languages = Languages(DEFAULT_LANGUAGE)

# ? core parts
db = Database(DATABASE_TOKEN, DATABASE_NAME, SUPER_ADMIN_ID, ADMIN_IDS)
bot = Bot(db, languages)
# dialogGenerator = DialogGenerator(bot, languages, db)

bot_plugins = MyBotPlugins(
    languages=languages, db=db, bot=bot
)

#? 
bot_plugins.set_languages(locales=[UK_LOCALE, RU_LOCALE], bot_language=DEFAULT_LANGUAGE)
bot_plugins.set_database()

#? Slash commands and user dialogs
bot_plugins.set_menu_commands()

# ? handlers
bot_handlers = BotHandlers(db, languages, bot)

common_handlers = CommonHandlers(db, languages, bot)
user_handlers = UserHandlers(db, languages, bot)
admin_handlers = AdminHandlers(db, languages, bot)

#? set handler 
bot_plugins.set_handlers(common_handlers)
bot_plugins.set_handlers(user_handlers)
bot_plugins.set_handlers(admin_handlers)

server = BotServer(bot=bot)
server.run()
