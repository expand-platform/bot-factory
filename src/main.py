#? bot engine
from bot_engine.capsules.Bots import Bots

#? config
from config.env import ACTIVE_BOT

bots = Bots(active_bot=ACTIVE_BOT)

bots.select_bot()

#! локальный / глобальный .env / разные .env для разных проектов (load_env как решение??)
#! локальные / глобальные конфиги (что и когда)
#! класс для капсулы (чтобы не копировать / вставлять, а создать единые API и менять его гибко (ГЕМОР))