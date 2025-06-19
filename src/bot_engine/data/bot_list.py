from dataclasses import dataclass

@dataclass
class BotList:
    TRADING_BOT: str = "trading-bot"
    SPORT_HOME_BOT: str = "sport-home-bot"
    PLATFORM_BOT: str = "platform-bot"
    REFERRAL_BOT: str = "referral-bot"

BOT_LIST = BotList() 