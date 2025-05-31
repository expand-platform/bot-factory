#? classes to work with 3rd-party API's
from dataclasses import field, dataclass
from typing import Any, Optional



@dataclass
class APIClient:
    TOKEN: str
    SECRET: Optional[str]
