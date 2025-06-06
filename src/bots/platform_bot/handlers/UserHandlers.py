from telebot import TeleBot
from telebot.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)

#? bot engine
from bot_engine.handlers.Handlers import Handlers
from bot_engine.enums.User import AccessLevel
from bot_engine.enums.Generator import *

#? constants
from bots.platform_bot.config.commands import BOT_COMMANDS
from bots.platform_bot.config.buttons import BOT_BUTTONS

#? enums
from bots.platform_bot.config.CallbackProperties import CallbackProperties
from bots.platform_bot.handlers.BotHandlers import BotHandlers


class UserHandlers(BotHandlers):
    """ creates user dialogs """

    def set_handlers(self, access_level=[AccessLevel.USER]):
        #? /start
        pass

        



        
      

       