from dataclasses import dataclass


@dataclass
class BotCommands:
    start: str = "start"
    conditions: str = "conditions"
    payment: str = "payment"
    prices: str = "prices"
    about: str = "about"
    info: str = "info"

    
BOT_COMMANDS = BotCommands()
