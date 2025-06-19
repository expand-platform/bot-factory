from telebot import TeleBot
from telebot.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)

#? bot engine
from bot_engine.handlers.Handlers import Handlers
from bot_engine.data.Users import AccessLevel
from bot_engine.enums.Generator import *

#? constants
from bots.referral_bot.config.BotCommands import BOT_COMMANDS
from bots.referral_bot.config.BotButtons import BOT_BUTTONS

#? enums
from bots.referral_bot.handlers.BotHandlers import BotHandlers


class UserHandlers(BotHandlers):
    """ creates user dialogs """

    def set_handlers(self, access_level=[AccessLevel.USER]):
        #? /start
        pass

        



        
      

       