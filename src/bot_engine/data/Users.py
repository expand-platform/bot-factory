from dataclasses import dataclass, field

@dataclass
class UserAction:
    SLASH_COMMAND: str = "slash_command"
    STATE: str = "state"
    INLINE_KEYBOARD: str = "inline_keyboard"
    REPLY_KEYBOARD: str = "reply_keyboard"
    

@dataclass
class CreateUserFrom:
    message: str = "message"
    database: str = "database"
    
@dataclass
class AccessLevel:
    SUPER_ADMIN: str = "super_admin"
    ADMIN: str = "admin"
    USER: str = "user"
    GUEST: str = "guest"
    
    
@dataclass
class CreateMethod:
    MESSAGE = "message"
    DATABASE = "database"
    

USER_ACTIONS = UserAction()
CREATE_USER_FROM = CreateUserFrom()
ACCESS_LEVEL = AccessLevel()