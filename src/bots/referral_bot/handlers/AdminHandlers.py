from telebot import TeleBot
from telebot.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)

from api.api_clients import API_CLIENTS

#? bot engine
from bot_engine.handlers.Handlers import Handlers
from bot_engine.data.Users import AccessLevel
from bot_engine.enums.Generator import *

#? constants
from bots.referral_bot.config.BotCommands import BOT_COMMANDS
from bots.referral_bot.config.BotButtons import BOT_BUTTONS

#? enums
from bots.referral_bot.handlers.BotHandlers import BotHandlers


class AdminHandlers(BotHandlers):
    """ creates user dialogs """

    def set_handlers(self, access_level=[AccessLevel.ADMIN, AccessLevel.SUPER_ADMIN]):
        pass
        # ? /start
        # @self._bot.message_handler(commands=[BOT_COMMANDS.admin_test], access_level=access_level)
        # def handle_start(message: Message):
        #     self._bot.reply_to(message, self._messages[BOT_COMMANDS.admin_test])

        
        



        
      

       