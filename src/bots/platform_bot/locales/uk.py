from telebot.types import BotCommand

#? engine
from bot_engine.languages.Locale import Locale

#? constats
from bots.platform_bot.config.commands import BOT_COMMANDS

UK_LOCALE = Locale(
    language_name="uk",

    command_descriptions = {
        BOT_COMMANDS.start: "Старт",
    },

    button_texts={},
    
    messages= {
        BOT_COMMANDS.start: "Привiт, {}! Чудовий день, чи не так?",
    }
)
