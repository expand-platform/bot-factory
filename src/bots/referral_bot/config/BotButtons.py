from dataclasses import dataclass

@dataclass
class BotButtons:
    languages: str = "languages"
    

@dataclass
class CallbackProperties:
    language: str = "language"

BOT_BUTTONS = BotButtons()