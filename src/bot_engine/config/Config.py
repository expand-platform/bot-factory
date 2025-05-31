from dataclasses import dataclass
from typing import Optional


@dataclass
class Config:
    """ sets bot-level config (local level) """
    database_name: str
    default_language: Optional[str] = "uk"

    #? optional
    users_collection: str = "users"
    products_collection: str = "products"
    database_connections_limit: Optional[int] = 1
    replica_name: Optional[str] = ""

    #? bot settings
    user_id_key: Optional[str] = "user_id"
    chat_id_key: Optional[str] = "chat_id"
