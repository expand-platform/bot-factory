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
from bot_engine.handlers.Handlers import Handlers
from bot_engine.users.User import User
from bot_engine.database.MongoDB import MongoDB
from bot_engine.bot.Bot import Bot
from bot_engine.database.Cache import Cache
from bot_engine.database.Database import Database
from bot_engine.languages.Languages import Languages

# ? const / enums
from bot_engine.const.Bot import *
from bot_engine.enums.User import *
from bot_engine.enums.Generator import *

#? own
from config.env import SUPER_ADMIN_ID, ADMIN_IDS
from bots.platform_bot.config.commands import BOT_COMMANDS



@dataclass
class BotHandlers(Handlers):
    """ custom handlers using Handler logic """
    pass