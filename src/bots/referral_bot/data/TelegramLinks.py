from dataclasses import dataclass

USERNAME = "@"
TG_DOMAIN = "https://t.me/"

@dataclass
class TelegramLinks:
    """ usernames """
    best_prepod: str = f"{USERNAME}best\\_prepod"
    damir_teacher: str = f"{USERNAME}damir\\_teacher"
    platform_bot: str = f"{USERNAME}expand\\_platform\\_bot"
    
    """ external links """
    platform_bot_link: str = f"{TG_DOMAIN}expand_platform_bot"
    

TELEGRAM_LINKS = TelegramLinks()


