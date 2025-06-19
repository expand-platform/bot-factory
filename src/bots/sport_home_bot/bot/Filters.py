from telebot.types import Message
from telebot.custom_filters import AdvancedCustomFilter

from bot_engine.data.Users import *
from bots.sport_home_bot.database.mongodb import Database

access_level_key = "access_level"


class SimpleAccessLevelFilter(AdvancedCustomFilter):
    """ checks user's AccessLevel """
    key = access_level_key

    def __init__(self, database: Database):
        self.db = database


    def check(self, message: Message, access_levels: list[AccessLevel]):
        user_id = message.from_user.id
        user = self.db.get_user_by_id(user_id)
        
        if not user:
            return False
        
        return AccessLevel(user[access_level_key]) in access_levels