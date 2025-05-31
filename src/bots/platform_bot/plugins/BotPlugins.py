from dataclasses import dataclass, field

from bot_engine.bot.BotConfigs import BotPlugins

#? engine customization
from bots.platform_bot.handlers.UserDialogs import UserDialogs
from bots.platform_bot.handlers.AdminDialogs import AdminDialogs

@dataclass
class MyBotPlugins(BotPlugins):

    def set_bot_dialogs(self):
        """ Prepares user and admin dialogs """
        UserDialogs(self.bot, self.dialogGenerator, self.languages).create_dialogs()
        AdminDialogs(self.bot, self.dialogGenerator, self.languages).create_dialogs()


