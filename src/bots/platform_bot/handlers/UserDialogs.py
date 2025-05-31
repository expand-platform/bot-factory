#? bot engine
from bot_engine.dialogs.BotDialogs import BotDialogs
from bot_engine.enums.User import AccessLevel
from bot_engine.enums.Generator import *

#? constants
from bots.platform_bot.config.commands import BOT_COMMANDS
from bots.platform_bot.config.buttons import BOT_BUTTONS

#? enums
from bots.platform_bot.config.CallbackProperties import CallbackProperties



class UserDialogs(BotDialogs):
    """ creates user dialogs """

    
    #! 3. Здесь делаем эти самые команды-диалоги
    def create_dialogs(self):
        """ 
            Use self.dialog_generator to generate user / admin dialogs.
            
            Example: 
            self.DialogGenerator.make_dialog(...) (see templates)
        """
        #! Разделить message в Language на userMessages и adminMessages
        messages = self.languages.get_messages()
        button_texts = self.languages.get_button_texts()
        
        #? /start: просит выбрать пункт меню
        self.dialogGenerator.make_dialog(
            command_name=BOT_COMMANDS.start,
            first_message=messages[BOT_COMMANDS.start],
        )
        
        #? /learn: просит выбрать пункт меню
        self.dialogGenerator.make_dialog(
            command_name=BOT_COMMANDS.learn,
            first_message=messages[BOT_COMMANDS.learn],
        )
        
        #? /about: о платформе
        self.dialogGenerator.make_dialog(
            command_name=BOT_COMMANDS.about,
            first_message=messages[BOT_COMMANDS.about],
        )
        
        #? /prices: цены на обучение
        self.dialogGenerator.make_dialog(
            command_name=BOT_COMMANDS.prices,
            first_message=messages[BOT_COMMANDS.prices],
        )
        
        #? /ask: задать вопрос
        self.dialogGenerator.make_dialog(
            command_name=BOT_COMMANDS.ask,
            first_message=messages[BOT_COMMANDS.ask],
        )

        #? /start - languages
        # self.dialogGenerator.make_dialog(
        #     command_name=BOT_COMMANDS.start,
        #     first_message=messages[BOT_COMMANDS.languages],
        #     # message_text=messages[BOT_COMMANDS.start],
        #     # inline_button_texts=button_texts[BOT_BUTTONS.languages],
        #     # inline_buttons_callback_property=CallbackProperties.language,
        #     # active_state=None,
        #     # save_to_state=None,
        # )

       