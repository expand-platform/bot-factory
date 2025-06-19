from dataclasses import dataclass, field

from typing import List, Optional, Any
from telebot.types import Message

# ? bot engine
from bots.trading_bot.config.env import ADMIN_IDS, SUPER_ADMIN_ID
from bot_engine.users.User import User, UserProfile, NewUser
from bot_engine.database.MongoDB import MongoDB
from bot_engine.database.Cache import Cache
from bot_engine.data.Users import CreateMethod, AccessLevel
from bot_engine.enums.Database import DatabaseAdapter


@dataclass
class Database:
    """
    Higher-level class for manipulating data in Database

    DB inlcudes MongoDB (remote data) and Cache (locale data) - users, products, versions

    Cache is used for fast data lookup (no need to send reduntant database requests)

    Cache and MongoDB are private classes
    Don't use them. Instead, user predefined methods like add_user or remove_user

    """

    #! in future: add support for multiple drivers: mongoDB or SQLite3 or another driver
    TOKEN: str
    DATABASE_NAME: str
    SUPER_ADMIN_ID: int
    ADMIN_IDS: list[int] | int
    USER_IDS: Optional[list[int]] = None

    adapter: DatabaseAdapter = DatabaseAdapter.MONGODB
    _database: MongoDB = field(init=False)
    _cache: Cache = field(init=False)


    def __post_init__(self):
        self.setup_database()


    #? inital setup
    def setup_database(self):
        """ runs post init setup """
        self.set_adapter()
        self.enable_cache()


    def set_adapter(self):
        if self.adapter == DatabaseAdapter.MONGODB:
            self._database = MongoDB(
                TOKEN=self.TOKEN,
                DATABASE_NAME=self.DATABASE_NAME,
                SUPER_ADMIN_ID=self.SUPER_ADMIN_ID,
            ) 
        else:
            print("❌CRITICAL: another database adapters is not found")
            pass


    def enable_cache(self):
        self._cache = Cache(SUPER_ADMIN_ID=self.SUPER_ADMIN_ID)


    def get_users(self):
        return self._cache._cached_users


    def add_user(self, new_user: User):
        self._database.add_user(new_user)
        self._cache.cache_user(new_user)


    def add_users(self, users: list[User]):
        """saves user to MongoDB and Cache"""
        for user in users:
            self._database.add_user(user)
            self._cache.cache_user(user)
    

    def set_access_level(self, user_id: int) -> str:
        """ sets user access level """
        access_level = AccessLevel.USER
        
        if user_id == SUPER_ADMIN_ID:
            access_level = AccessLevel.SUPER_ADMIN
        
        elif user_id in ADMIN_IDS or user_id == ADMIN_IDS:
            access_level = AccessLevel.ADMIN
        
        #? in cases when bot is closed from other users  
        elif self.USER_IDS:
            if user_id in self.USER_IDS or user_id == self.USER_IDS: 
                access_level = AccessLevel.USER
            else:
                access_level = AccessLevel.GUEST
        
        return access_level
    

    def create_user(self, message: Optional[Message] = None, database_user: Optional[dict[str, str | int | bool]] = None) -> User:
        access_level = None
        new_user = None
        
        if message:
            access_level = self.set_access_level(user_id=message.from_user.id)
            new_user = NewUser(access_level).create_user(message=message)
            
        elif database_user:
            access_level = self.set_access_level(user_id=database_user.get("user_id"))
            new_user = NewUser(access_level).create_user(database_user=database_user)
            
        return new_user


    def get_active_user(self, message: Message) -> User:
        """get saved active user or create a new user"""
        active_user = self._cache.find_active_user_in_cache(user_id=message.from_user.id)
        
        # ? if no user, create it from message
        if active_user is None:
            print(f"👀 Wow, there's someone new here..")
            active_user = self.create_user(message)
            self._database.add_user(active_user)
            self.cache_user(active_user)

        return active_user
    

    # ? cache methods
    def cache_user(self, user: User):
        """cache user in Cache"""
        self._cache.cache_user(user)
        print(f"🤿 User {user.first_name} cached!")


    #! Автоматически детектить админов и суперадминов по их user_id
    def cache_users(self) -> None:
        """
        Caches users from database

        1. Cleans cache
        2. Fetches users from a DB
        3. Cache users

        """

        self._cache.clean_users()

        database_users = self._database.get_all_users()
        print(f"✨ Users in Database: { len(database_users) }")

        if database_users:
            for database_user in database_users:
                new_user = self.create_user(database_user=database_user)
                self._cache.cache_user(new_user)

            print(f"👥 Users in cache: { len(self._cache._cached_users) }")

        # ? else, cache.users == []
        else:
            print("✖ Cache is empty!")


    # ? update methods
    def update_user(self, user_id: int, key: str, new_value: str | int | bool):
        self._database.update_user(user_id, key=key, new_value=new_value)
        self._cache.update_user(user_id, key=key, new_value=new_value)

        print(f"📅 Пользователь обновлён (update_user): { user_id }")


    def update_real_name(self, user_id: int, new_value: str | int | bool):
        self.update_user(user_id=user_id, key="real_name", new_value=new_value)


    #! Нужно делать апдейт не чаще, чем раз в сутки. А то и раз в неделю.       
    def update_user_profile(self, active_user: User, message: Message):
        """ updates user profile from telegram message """
        profile = UserProfile(message)

        first_name = profile.get_first_name()
        username = profile.get_username()
        print("🐍 update_user_profile ~ first_name",first_name)
        print("🐍 update_user_profile ~ username",username)

        # ? update in DB
        self.update_user(active_user.user_id, "first_name", first_name)
        self.update_user(active_user.user_id, "username", username)


    # ? cleaning methods
    def clean_users(self):
        """cleans users in MongoDB and Cache"""
        self._database.clean_users()
        self._cache.clean_users()


    def remove_user(self, user_id: int) -> None:
        self._database.remove_user(user_id)
        self._cache.remove_user(user_id)
        print(f"User fully removed from Database!")
