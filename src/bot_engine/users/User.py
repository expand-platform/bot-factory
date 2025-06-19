from dataclasses import dataclass, asdict
from typing import Optional, Any
from datetime import datetime

# ? telebot
from telebot.types import Message

# ? configs
from config.env import ADMIN_IDS, DEFAULT_LANGUAGE, SUPER_ADMIN_ID

# ? data
from bot_engine.data.Users import AccessLevel

# ? engine
from bot_engine.languages.Languages import Languages


#! Нужно придумать систему, которая будет создавать разные типы
#! И систему, которая будет обновлять username раз в сутки / раз в неделю исходя из даты profile_update (чтобы не при каждом хендлере)


@dataclass
class User:
    first_name: str
    username: str

    user_id: int
    chat_id: int

    access_level: str

    language: str
    joined: str
    profile_updated: str

    is_premium: bool

    def to_dict(self):
        dict = asdict(self)
        return dict


@dataclass
class NewUser:
    """creates user from it's message data or from database"""
    access_level: str = AccessLevel.USER


    def create_user(
        self,
        message: Optional[Message] = None,
        database_user: Optional[dict[str, str | int | bool]] = None,
    ):
        """crafts user data depending on given source of data"""
        first_name = user_id = chat_id = username = None
        joined = profile_updated = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        language = DEFAULT_LANGUAGE
        access_level = self.access_level
        is_premium = False

        if message:
            first_name = message.from_user.first_name
            username = message.from_user.username

            user_id = message.from_user.id
            chat_id = message.chat.id

        elif database_user:
            first_name = database_user["first_name"]
            username = database_user["username"]

            user_id = database_user["user_id"]
            chat_id = database_user["chat_id"]


        if user_id == SUPER_ADMIN_ID:
            access_level, is_premium = self.make_admin(access_level=AccessLevel.SUPER_ADMIN)

        elif user_id in ADMIN_IDS:
            access_level, is_premium = self.make_admin(access_level=AccessLevel.ADMIN)


        return User(
            first_name=first_name,
            username=username or None,
            user_id=user_id,
            chat_id=chat_id,
            access_level=access_level,
            language=language,
            joined=joined,
            profile_updated=profile_updated,
            is_premium=is_premium,
        )


    def make_admin(self, access_level: str = AccessLevel.SUPER_ADMIN) -> list[str | bool]:
        """set access level and premium privileges"""
        is_premium = True
        return [access_level, is_premium]


@dataclass
class UserProfile:
    user_message: Message

    def get_first_name(self) -> str:
        """return user first_name"""
        return self.user_message.from_user.first_name or "not set"

    def get_username(self) -> str:
        """returns user @username"""
        return self.user_message.from_user.username or "not set"
