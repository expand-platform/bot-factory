from dataclasses import dataclass

@dataclass
class BotCommands:
    start: str = "start"
    learn: str = "learn"
    prices: str = "prices"
    ask: str = "ask"
    about: str = "about"
    languages: str = "languages"
    
BOT_COMMANDS = BotCommands()
