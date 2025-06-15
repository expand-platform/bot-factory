from os import environ

#? telebot
from telebot import TeleBot
from telebot.types import Message, BotCommand
from telebot.custom_filters import StateFilter, IsDigitFilter, TextMatchFilter
from telebot.states.sync.middleware import StateMiddleware


#? modules
from bots.sport_home_bot.bot.Filters import SimpleAccessLevelFilter
from bots.sport_home_bot.database.mongodb import Database
from bots.sport_home_bot.bot.exception_handler import ExceptionHandler
from bots.sport_home_bot.bot.helpers import Helpers

#? data
from bots.sport_home_bot.bot.messages import messages
from bots.sport_home_bot.bot.Commands import bot_commands
from config.env import SUPER_ADMIN_ID


class Bot:
    def __init__(self, database: Database):
        BOT_TOKEN = environ["BOT_TOKEN"]
        self.db = database
        self.messages = messages


        self._bot = TeleBot(BOT_TOKEN, exception_handler=ExceptionHandler(), use_class_middlewares=True)
        self.set_middleware()

        self.setup_command_menu()
        self._bot.send_message(chat_id=SUPER_ADMIN_ID, text="Starting bot...")



    def set_middleware(self) -> None:
        self._bot.add_custom_filter(StateFilter(self._bot))
        self._bot.add_custom_filter(IsDigitFilter())
        self._bot.add_custom_filter(TextMatchFilter())
        self._bot.add_custom_filter(SimpleAccessLevelFilter(self.db))

        self._bot.setup_middleware(StateMiddleware(self._bot))


    def setup_command_menu(self):
        commands = [
            BotCommand(command=bot_commands.add_product.name, description=bot_commands.add_product.description),
            BotCommand(command=bot_commands.remove_product.name, description=bot_commands.remove_product.description),
            BotCommand(command=bot_commands.parse.name, description=bot_commands.parse.description),
            BotCommand(command=bot_commands.info.name, description=bot_commands.info.description),
            BotCommand(command=bot_commands.set_time.name, description=bot_commands.set_time.description),
        ]
        self._bot.set_my_commands(commands)
