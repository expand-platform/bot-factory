from dataclasses import dataclass, field
from typing import Optional
from psutil import users

#? engine
from bot_engine.users.User import User, NewUser
from bot_engine.data.Users import AccessLevel


#! 1. Теперь здесь можно создавать переменные ячейки, например
#! передавать объект с ключами (лучше Enum) для создания каталогов Cache
# catalogs = [Cache.USERS, Cache.VERSIONS] и т.д

#! 2. Вернуть выпиленные initial users :( (не горит)

@dataclass
class Cache:
    SUPER_ADMIN_ID: int
    _cached_users: list[User] = field(init=False)  

    def __post_init__(self):
        #? clean start - no users in cache
        self._cached_users = []

            
    def cache_user(self, user: User) -> None:
        """ cache user if it's not in cache already """
        is_user_in_cache = self.check_if_user_in_cache(user.user_id)

        if not is_user_in_cache:
            self._cached_users.append(user)
        
        
    def get_users_from_cache(self) -> list:
        if len(self._cached_users) > 0:
            return self._cached_users
        else:
            return []
    
    
    def find_active_user_in_cache(self, user_id: int) -> User | None:
        print(f"user_id (Cache.find_active_user): { user_id }")
        
        for user in self._cached_users:
            if user.user_id == user_id:
                print(f"🟢 User {user_id} found in cache")
                return user

        print(f"🔴 User {user_id} isn't found in cache")
        return None
    

    def update_user(self, user_id: int, key: str, new_value: str | int | bool):
        """ updates user in cache"""
        print(f"Updating user with id {user_id} in cache..")

        for user in self._cached_users:
            if user.user_id == user_id:
                setattr(user, key, new_value)

                print(f"🍏 Update user: {user_id} updated with '{key}'='{new_value}'")
                break
                

    def get_user(self, user_id: int) -> Optional[User]:
        for user in self._cached_users:
            if user.user_id == user_id:
                return user
            
            
    def remove_user(self, user_id: int) -> None:
        for cache_user in self._cached_users:
            if user_id == cache_user.user_id:
                self._cached_users.remove(cache_user)
                print(f"User removed from cache!")
                
    
    def check_if_user_in_cache(self, user_id: int) -> bool:
        for user in self._cached_users:
            if user.user_id == user_id:
                print(f"🟢 user exists in Cache: {user_id}")
                return True
        print(f"🟡 user doesn't exists in Cache: {user_id}, caching...")
        return False
        

    
    def find_user_by_property(self, property_name, value):
        for user in self._cached_users:
            if property_name in user:
                if value == user[property_name]:
                    print("🐍 user (find_user_by_property): ",user)
                    return user
                

    def clean_users(self):
        """ cleans all users, except super_admin """
        self._cached_users = []
        print(f"Кеш пользователей очищен! 🧹\n{self._cached_users}")
