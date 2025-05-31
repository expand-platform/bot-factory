from dataclasses import dataclass
from telebot.types import BotCommand
#? bot engine
from bot_engine.languages.Locale import Locale

#? constats
from bots.trading_bot.config.commands import BOT_COMMANDS
from bots.trading_bot.config.buttons import BOT_BUTTONS



RU_LOCALE = Locale(
    language_name="ru",

    command_descriptions = {
        BOT_COMMANDS.start: "Старт",
        BOT_COMMANDS.btc_price: "Цена Bitcoin",     
        BOT_COMMANDS.user_test: "User test command",     
        BOT_COMMANDS.admin_test: "Admin test command",    
    },

    button_texts = {
    },

    messages= { 
        BOT_COMMANDS.start: [
            "Привiт! Я - бот-помiчник для трейдингу",
        ], 
        BOT_COMMANDS.btc_price: [
            "Цена Bitcoin сейчас: ",
        ], 
        BOT_COMMANDS.user_test: [
            "User test command",
        ], 
        BOT_COMMANDS.admin_test: [
            "Admin test command",
        ],  
    }
)
