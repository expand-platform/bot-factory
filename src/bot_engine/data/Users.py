from dataclasses import dataclass, field


@dataclass
class UserAction:
    SLASH_COMMAND: str = "slash_command"
    STATE: str = "state"
    INLINE_KEYBOARD: str = "inline_keyboard"
    REPLY_KEYBOARD: str = "reply_keyboard"

USER_ACTIONS = UserAction()