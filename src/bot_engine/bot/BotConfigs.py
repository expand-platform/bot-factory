from dataclasses import dataclass, field
from typing import Any

#? engine
from bot_engine.languages.Locale import Locale
from bot_engine.languages.Languages import Languages
from bot_engine.bot.Bot import Bot
from bot_engine.database.Database import Database

#? config
from config.env import DEFAULT_LANGUAGE


@dataclass
class BotPlugins:
    """ 
        Bot dependencies manager. 
        You can customize this class by extending its methods 

        set_database()
        set_languages()
        set_menu_commands()
        set_dialog_generator()
        set_bot_dialogs()
        set_extra_settings()

        or you can use set_all and pass all data there (*future)

    """
    languages: Languages
    db: Database
    bot: Bot

    handlers: Any = field(init=False)
    # dialogGenerator: DialogGenerator
    
    def set_database(self):
        """ Connects MongoDB, prepares cache for users """
        #? Prepare users in cache for further interactions  
        self.db.cache_users()

    #! Create list of constants of supported API clients
    # def add_api_client(self, client_name: str, client: Any):
    #     """ sets global access to API client for all bot components """
    #     self.dialogGenerator.add_api_client(client_name=client_name,client=client)
    #     print(f"🟢 API client {client_name} set!")


    def set_languages(self, locales: list[Locale], bot_language = DEFAULT_LANGUAGE):
        """ sets locales and active language """
        for locale in locales:
            self.languages.add_locale(locale)

        self.languages.set_active_language(bot_language)
        print(f"🌐 {bot_language } language set!")


    def set_menu_commands(self):
        """ Sets bot menu commands """
        menu_commands = self.languages.get_menu_commands()
        
        self.bot._bot.set_my_commands([])
        self.bot._bot.set_my_commands(commands=menu_commands)
        print("🔉 Slash commands set!")



    # def set_dialog_generator(self):
    #     """ Prepares DialogGenerator for work """
    #     pass

    # def set_bot_handlers(self, handlersClass: Any):
    #     self.handlers = handlersClass


    def set_handlers(self):
        """ Prepares user and admin dialogs """
        pass

    def set_extra_settings(self):
        """ You can define your extra setup settings here """
        pass

