# ? configs
from bots.platform_bot.config.langConfig import DEFAULT_LANGUAGE
from config.env import DATABASE_TOKEN, SUPER_ADMIN_ID, ADMIN_IDS
from bots.platform_bot.config.dbConfig import DATABASE_NAME
from bots.platform_bot.config.langConfig import DEFAULT_LANGUAGE

# ? bot engine
from bot_engine.bot.Bot import Bot
from bot_engine.dialogs.DialogGenerator import DialogGenerator
from bot_engine.languages.Languages import Languages
from bot_engine.database.Database import Database

# ? engine customization
from bots.platform_bot.plugins.BotPlugins import MyBotPlugins
from bots.platform_bot.server.BotServer import BotServer

# ? languages
from bots.platform_bot.locales.uk import UK_LOCALE
from bots.platform_bot.locales.ru import RU_LOCALE 

# ? dialogs
from bots.platform_bot.handlers.AdminDialogs import AdminDialogs


languages = Languages(DEFAULT_LANGUAGE)

# ? core parts
db = Database(DATABASE_TOKEN, DATABASE_NAME, SUPER_ADMIN_ID, ADMIN_IDS)
bot = Bot(db, languages)
dialogGenerator = DialogGenerator(bot, languages, db)

bot_configs = MyBotPlugins(
    languages=languages, db=db, bot=bot
)

#? 
bot_configs.set_languages(locales=[UK_LOCALE, RU_LOCALE], bot_language=DEFAULT_LANGUAGE)
bot_configs.set_database()

#? Slash commands and user dialogs
bot_configs.set_menu_commands()
bot_configs.set_bot_dialogs()


server = BotServer(bot=bot)
server.run()
