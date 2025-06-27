from dotenv import load_dotenv, dotenv_values
from pymongo.collection import Collection, ObjectId
from pymongo.mongo_client import MongoClient
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union

from config.env import DATABASE_TOKEN

#? bot settings
from bots.sport_home_bot.config.Config import BOT_CONFIGS

@dataclass
class ConfigDocument:
    _id: str = "_id"
    parse_time: str = "parse_time"

@dataclass
class ProductDocument:
    _id: str = "_id"
    id: str = "id"


@dataclass
class StatisticsDocument:
    _id: str = "_id"
    products_tracked: str = "products_tracked"

@dataclass
class Collections:
    config: str = "config"
    stats: str = "stats"


CONFIG_DOCUMENT = ConfigDocument()
PRODUCT_DOCUMENT = ProductDocument()
STATS_DOCUMENT = StatisticsDocument()

DB_COLLECTIONS = Collections()


#! We'll need to use bot_engine Database & MongoDB classes later
class Database():
    def __init__(self) -> None:
        self.client = MongoClient(DATABASE_TOKEN)
        self.db = self.client[BOT_CONFIGS.database_name]
        self.users_collection = self.db[BOT_CONFIGS.users_collection]
        self.products_collection = self.db[BOT_CONFIGS.products_collection]
        
        """ collections """
        self.config_collection = self.db[DB_COLLECTIONS.config]
        self.stats_collection = self.db[DB_COLLECTIONS.stats]

        
    def get(self, key: str, collection_name: str = DB_COLLECTIONS.config) -> list[dict]:
        """ returns list of documents from given collection """
        return list(self.db[collection_name].find({}))


    def insert_product(self, product: Dict[str, Any]) -> None:
        try:
            status = self.products_collection.find_one({"id": product["id"]})
            if status:
                print("Product already exists in the database")
                return
            else:
                self.products_collection.insert_one(product)
                print("Product inserted into database")
        except Exception as e:
            print(f"An error occurred: {e}")

        
    def get_products(self) -> List[Dict[str, Any]]:
        try:
            products = list(self.products_collection.find({}))
            return products
        except Exception as e:
            print(f"An error occurred: {e}")
            return []



    def insert_user(self, user: Dict[str, Any]) -> None:
        try:
            status = self.users_collection.find_one({"chat_id": user["chat_id"]})
            if status:
                print("User already exists in the database")
                return
            else:
                self.users_collection.insert_one(user)
                print("User inserted into database")
        except Exception as e:
            print(f"An error occurred: {e}")

    
    def get_user_by_id(self, user_id: Union[int, str]) -> Optional[Dict[str, Any]]:
        try:
            return self.users_collection.find_one({"chat_id": user_id})
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_users(self) -> List[Dict[str, Any]]:
        try:
            users = list(self.users_collection.find())
            return users
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def find(self, key: str, value: Union[str, int, bool, list]) -> Optional[Dict[str, Any]]:
        return self.products_collection.find_one({key: value})
        

    def update(self, key: str, value: Any, field_name: str, new_value: Any) -> None:
        try:
            self.products_collection.update_one({key: value}, {"$set": {field_name: new_value}})
            print(f"Updated {field_name} to {new_value} for {key}: {value}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
     
    def update_one_document(self, collection_name: str = "config", key: str = "", value: Union[str, int, bool] = "") -> None:
        """ updates one document in collection """
            
        document: dict = self.db[collection_name].find_one({})

        if document:
            document_id = document[CONFIG_DOCUMENT._id]
        else:
            print(f"🔴 No config document found!")
            return
        
        update_data = {'$set': {key: value}}
        result = self.db[collection_name].update_one({'_id': ObjectId(document_id)}, update_data)
        
        if result.modified_count > 0:
            print(f"🟢 Config updated: {key}:{value}")

        elif result.matched_count > 0:
            print("🟡 Nothing new in config")
        
        else:
            print("🔴 Error: no such _id or document in config collection")


    def get_parse_time(self) -> List[int]:
        document = self.config_collection.find_one({})

        parse_time = [19, 0]

        if document is None:
            #? set default time
            document = {
                CONFIG_DOCUMENT.parse_time: parse_time
            }
            self.config_collection.insert_one(document)

        else:
            parse_time = document[CONFIG_DOCUMENT.parse_time]

            #? set default time
            for time in parse_time:
                if time is None:
                    parse_time = [19, 0]
            
        return parse_time
        

    #? REMOVALS
    def remove_product(self, id: int) -> None:
        document = self.products_collection.delete_one({PRODUCT_DOCUMENT.id: id})

        if document:
            print(f"🟢 product {id} deleted from DB!")
        else:
            print(f"🟡 Product with {id} not found in DB!")
            
            
    
    #? STATS    
    def get_products_count(self) -> int:
        return len(self.get_products())
    
    def get_products_tracked_stats(self) -> int:
        document = self.stats_collection.find_one({})
        return document[STATS_DOCUMENT.products_tracked]       


