from dataclasses import dataclass


@dataclass
class BotCommands:
    start: str = "start"
    ask: str = "ask"
    prices: str = "prices"
    about: str = "about"
    help: str = "help"

    
BOT_COMMANDS = BotCommands()
