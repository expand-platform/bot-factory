from dataclasses import dataclass, field

#? bot-engine
from bot_engine.bot.BotConfigs import BotPlugins
from bots.referral_bot.handlers.BotHandlers import BotHandlers


@dataclass
class MyBotPlugins(BotPlugins):
    def set_handlers(self, handlers: BotHandlers):
        handlers.set_handlers()
        print(f"🟢 Bot handlers set!")
        




