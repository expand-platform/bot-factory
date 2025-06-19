from dataclasses import dataclass, field

from telebot import TeleBot

from bot_engine.bot.Bot import Bot


@dataclass
class HandlerHelpers:
    _bot: Bot

    def format_message(
        self, message: str, format_variables: dict[str, str | int]
    ) -> str:

        if isinstance(message, list):
            message = "".join(message)

        format_variables = self.make_safe_variables(format_variables)
        return message.format_map(format_variables)
    

    def make_safe_variables(self, format_variables: dict[str, str | int] ) -> dict[str, str | int]:
        for key, value in format_variables.items():
            if value and "_" in value:
                format_variables[key] = value.replace("_", "\\_")

        return format_variables


    def notify_super_admin(
        self, message: str, format_variables: dict[str, str | int]
    ) -> None:
        super_admin_notification = self.format_message(
            message=message,
            format_variables=format_variables,
        )
        self._bot.tell_super_admin(messages=[super_admin_notification])
