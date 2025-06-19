from typing import Union, TYPE_CHECKING
from telebot.custom_filters import AdvancedCustomFilter
from telebot.types import Message, CallbackQuery

#? bot engine
from bot_engine.data.Users import *

# ? engine types
if TYPE_CHECKING:
    from bot_engine.database.Database import Database
    from bot_engine.languages.Languages import Languages


class AccessLevelFilter(AdvancedCustomFilter):
    key = "access_level"

    def __init__(self, db: "Database", languages: "Languages"):
        self.database = db
        self.languages = languages


    def check(self, message: Union[Message, CallbackQuery], access_level: list[AccessLevel]):
        print(f"🔍 Filters (check)")
        active_user = None

        #? inline keyboard reply filters bot itself
        if not hasattr(message, "chat"):
            active_user = self.database.get_active_user(message)
            message = message.message
        else: 
            active_user = self.database.get_active_user(message)

        user_access_level = active_user.access_level

        #? Смена языка пользователя
        self.languages.set_active_language(active_user.language)

        access_level_values = [level for level in access_level]
        return user_access_level in access_level_values


