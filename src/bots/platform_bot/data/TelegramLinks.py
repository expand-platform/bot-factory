from dataclasses import dataclass

USERNAME = "@"
DOMAIN = "https://t.me/"

@dataclass
class TelegramLinks:
    """ me """
    best_prepod: str = f"{USERNAME}best\\_prepod"
    damir_teacher: str = f"{USERNAME}damir\\_teacher"
    

TELEGRAM_LINKS = TelegramLinks()


