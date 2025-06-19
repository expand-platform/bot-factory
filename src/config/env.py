#? bot engine
from bot_engine.utils.Dotenv import Dotenv

dotenv = Dotenv()

#? bots
ACTIVE_BOT: str = dotenv.get("ACTIVE_BOT") or "" 
BOT_TOKEN: str = dotenv.get("BOT_TOKEN") or "" 

#? configs
ENVIRONMENT: str = dotenv.get("ENVIRONMENT") or "DEVELOPMENT" 
PORT: int = dotenv.get_int("PORT") or 8000
DEFAULT_LANGUAGE = dotenv.get("DEFAULT_LANGUAGE") or "ru" 

#? DB
DATABASE_TOKEN: str = dotenv.get("DATABASE_TOKEN") or "" 
SUPER_ADMIN_ID: int = dotenv.get_int("SUPER_ADMIN_ID")
ADMIN_IDS: list[int] = dotenv.get_list_of_ints("ADMIN_IDS")

#? APIs
BINANCE_TOKEN: str = dotenv.get("BINANCE_API_KEY") or "" 
BINANCE_SECRET: str = dotenv.get("BINANCE_SECRET_KEY") or "" 

BINANCE_TESTNET_TOKEN: str = dotenv.get("BINANCE_TESTNET_API_KEY") or "" 
BINANCE_TESTNET_SECRET: str = dotenv.get("BINANCE_TESTNET_SECRET_KEY") or "" 
