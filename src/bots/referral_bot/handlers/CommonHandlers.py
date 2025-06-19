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


class CommonHandlers(BotHandlers):
    """ creates dialogs for any access_level """

    def set_handlers(self, access_level=[AccessLevel.USER, AccessLevel.ADMIN, AccessLevel.SUPER_ADMIN]):
        
        #? /start
        self.slash_command(
            command=BOT_COMMANDS.start,
            messages=self._messages[BOT_COMMANDS.start],
        )
        
        #? /conditions
        self.slash_command(
            command=BOT_COMMANDS.conditions,
            messages=self._messages[BOT_COMMANDS.conditions],
        )

        #? /how_much
        self.slash_command(
            command=BOT_COMMANDS.payment,
            messages=self._messages[BOT_COMMANDS.payment],
        )

        #? /prices
        self.slash_command(
            command=BOT_COMMANDS.prices,
            messages=self._messages[BOT_COMMANDS.prices],
        )
        
        #? /about
        self.slash_command(
            command=BOT_COMMANDS.about,
            messages=self._messages[BOT_COMMANDS.about],
        )
        
        #? /info
        self.slash_command(
            command=BOT_COMMANDS.info,
            messages=self._messages[BOT_COMMANDS.info],
        )



        



        
      

       