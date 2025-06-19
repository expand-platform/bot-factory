from dataclasses import dataclass

@dataclass
class Triggers:
    """ index """
    slash_command: str = "slash_command"
    

USER_ACTIONS = Triggers()


