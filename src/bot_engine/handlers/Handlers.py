from dataclasses import dataclass, field
from typing import Any, Callable, ClassVar, Optional, Union

from telebot import TeleBot
from telebot.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)
from telebot.states.sync.context import StateContext

from binance import Client

# ? bot engine
from api.BinanceAPI import BinanceAPI
from bot_engine.bot.Bot import Bot
from bot_engine.users.User import NewUser
from bot_engine.database.MongoDB import MongoDB
from bot_engine.database.Cache import Cache
from bot_engine.database.Database import Database
from bot_engine.languages.Languages import Languages
from bot_engine.data.Users import USER_ACTIONS
from bot_engine.handlers.HandlerHelpers import HandlerHelpers

# ? const / enums
from bot_engine.const.Bot import *
from bot_engine.data.Users import *
from bot_engine.enums.Generator import *

# ? own
from bots.trading_bot.config.env import SUPER_ADMIN_ID, ADMIN_IDS


@dataclass
class Handlers:
    """ready-to-use handlers solutions, logic and helpers"""

    database: Database
    languages: Languages
    bot: Bot

    # ? API clients
    _api_clients: ClassVar[dict[str, BinanceAPI | Any]] = {}

    # ? private variables
    _bot: TeleBot = field(init=False)
    _messages: dict = field(init=False)
    _buttons: dict = field(init=False)
    _Helpers: HandlerHelpers = field(init=False)


    def __post_init__(self):
        self._bot = self.bot._bot
        self._messages = self.languages.get_messages()
        self._buttons = self.languages.get_button_texts()

        self._Helpers = HandlerHelpers(self.bot)


    def set_handlers(self):
        """reusable method for creating handlers with specific access level"""
        pass


    def add_api_client(self, client_name: str, client_api: BinanceAPI | Any):
        """sets API to work with"""
        self._api_clients[client_name] = client_api
        print("🐍 self.api_clients", self._api_clients[client_name])
        print(f"🟢 API for {client_name} set!")


    def slash_command(
        self,
        messages: str | list[str],
        command: str,
        access_level: list[AccessLevel] = [
            AccessLevel.USER,
            AccessLevel.ADMIN,
            AccessLevel.SUPER_ADMIN,
        ],
    ):
        @self._bot.message_handler(commands=[command], access_level=access_level)
        def handle_start(message: Message):
            self.bot._send_message(chat_id=message.chat.id, messages=messages)
            
            if message.chat.id != SUPER_ADMIN_ID:  
                notification = "{first_name} @{username} перешёл в /{slash_command}"
                self._Helpers.notify_super_admin(
                    message=notification,
                    format_variables={
                        "first_name": message.from_user.first_name,
                        "username": message.from_user.username,
                        "slash_command": command,
                    },
                )

    def slash_command_reply(
        self,
        message: Message,
        command_name: str,
        access_level: list[AccessLevel] | AccessLevel,
        database_action: Optional[str] = None,
        api_action: Optional[str] = None,
    ):
        """creates simple message reply for a /slash command using api / database data [optional]"""
        pass
