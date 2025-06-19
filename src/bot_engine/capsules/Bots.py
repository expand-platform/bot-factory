from dataclasses import dataclass
from typing import Optional

#? config
from bot_engine.data.bot_list import BOT_LIST


@dataclass
class Bots:
    """ Handles multiple bots in the project (Bot Capsules) """
    active_bot: Optional[str]

    def select_bot(self):
        """ manages bot file / class imports """
        if self.active_bot == BOT_LIST.TRADING_BOT:
            from bots.trading_bot import main
        
        elif self.active_bot == BOT_LIST.PLATFORM_BOT:
            from bots.platform_bot import main
        
        elif self.active_bot == BOT_LIST.SPORT_HOME_BOT:
            from bots.sport_home_bot import main
        
        elif self.active_bot == BOT_LIST.REFERRAL_BOT:
            from bots.referral_bot import main

        else:
            raise Exception("❌ Active bot isn't choose, please double-check 'ACTIVE_BOT' in .env file")
        