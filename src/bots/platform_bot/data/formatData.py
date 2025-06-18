from dataclasses import dataclass

@dataclass
class FormatData:
    """ index """
    first_name: str = "first_name"
    username: str = "username"
    user_id: str = "id"
    

FORMAT_DATA = FormatData()


