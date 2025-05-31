from dataclasses import dataclass
from bot_engine.config.Config import Config


class BotConfig(Config):
    pass


BOT_CONFIGS = BotConfig(
    database_name = "zelart-parser",
    default_language = "uk"
)