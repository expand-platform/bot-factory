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
from bots.trading_bot.config.commands import BOT_COMMANDS
from bots.trading_bot.config.buttons import BOT_BUTTONS

#? enums
from bots.trading_bot.config.CallbackProperties import CallbackProperties

from bots.trading_bot.handlers.BotHandlers import BotHandlers


class UserHandlers(BotHandlers):
    """ creates user dialogs """

    def set_handlers(self, access_level=[AccessLevel.USER]):
        #? /start
        @self._bot.message_handler(commands=[BOT_COMMANDS.user_test], access_level=access_level)
        def handle_start(message: Message):
            self._bot.reply_to(message, self._messages[BOT_COMMANDS.user_test])

        



        
      

       