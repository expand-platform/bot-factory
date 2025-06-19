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
from bots.trading_bot.config.commands import BOT_COMMANDS
from bots.trading_bot.config.buttons import BOT_BUTTONS

#? enums
from bots.trading_bot.config.CallbackProperties import CallbackProperties

from bots.trading_bot.handlers.BotHandlers import BotHandlers


class CommonHandlers(BotHandlers):
    """ creates dialogs for any access_level """

    def set_handlers(self, access_level=[AccessLevel.USER, AccessLevel.ADMIN, AccessLevel.SUPER_ADMIN]):
        #? /start
        @self._bot.message_handler(commands=[BOT_COMMANDS.start], access_level=access_level)
        def handle_start(message: Message):
            self._bot.reply_to(message, "Hi! Send /price to get the current BTC price.")

        #? /btc_price
        @self._bot.message_handler(commands=[BOT_COMMANDS.btc_price], access_level=access_level)
        def handle_price(message):
            print(self._api_clients)
            try:
                price = self._api_clients[API_CLIENTS.Binance].get_btc_price()
                self._bot.reply_to(message, f"Current BTC price: ${price}")
            except Exception as e:
                self._bot.reply_to(message, "Sorry, I couldn't fetch the price.")
        
        @self._bot.message_handler(commands=[BOT_COMMANDS.limits], access_level=access_level)
        def exchange_info(message):
            print(self._api_clients)
            try:
                print(1)
                price = self._api_clients[API_CLIENTS.Binance].get_btc_price()
                self._bot.reply_to(message, f"Current BTC price: ${price}")
            except Exception as e:
                self._bot.reply_to(message, "Sorry, I couldn't fetch the price.")
        



        
      

       