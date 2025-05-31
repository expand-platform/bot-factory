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
from bot_engine.enums.User import AccessLevel
from bot_engine.enums.Generator import *

#? constants
from bots.platform_bot.config.commands import BOT_COMMANDS
from bots.platform_bot.config.buttons import BOT_BUTTONS

#? enums
from bots.platform_bot.config.CallbackProperties import CallbackProperties

from bots.platform_bot.handlers.BotHandlers import BotHandlers


class CommonHandlers(BotHandlers):
    """ creates dialogs for any access_level """

    def set_handlers(self, access_level=[AccessLevel.USER, AccessLevel.ADMIN, AccessLevel.SUPER_ADMIN]):
        
        #? /start
        self.send_message_reply(
            for_command=BOT_COMMANDS.start,
            messages=self._messages[BOT_COMMANDS.start],
        )
        
        #? /learn
        self.send_message_reply(
            for_command=BOT_COMMANDS.learn,
            messages=self._messages[BOT_COMMANDS.learn],
        )
        
        #? /prices
        self.send_message_reply(
            for_command=BOT_COMMANDS.prices,
            messages=self._messages[BOT_COMMANDS.prices],
        )

        #? /ask
        self.send_message_reply(
            for_command=BOT_COMMANDS.ask,
            messages=self._messages[BOT_COMMANDS.ask],
        )

        #? /about
        self.send_message_reply(
            for_command=BOT_COMMANDS.about,
            messages=self._messages[BOT_COMMANDS.about],
        )



        



        
      

       