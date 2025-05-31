from dataclasses import dataclass, field
from typing import Optional



@dataclass
class BotCommands:
    start: str = "start"
    btc_price: str = "btc_price"
    user_test: str = "user_test"
    admin_test: str = "user_test"
    limits: str = "limits"

BOT_COMMANDS = BotCommands()
