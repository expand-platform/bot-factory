from dataclasses import field, dataclass
from typing import Any, Optional

#? bot-specific
from binance.client import Client

from api.api import APIClient


@dataclass
class BinanceAPI(APIClient):
    """ class for working with Binance API """
    _client: Client = field(init=False)

    def __post_init__(self):
        """ creates a client / connection to API """
        self._client: Client = Client(api_key=self.TOKEN, api_secret=self.SECRET) 
        # print("🐍 File: api/api.py | Line: 36 | __post_init__ ~ self._client",self._client)

    def get_btc_price(self) -> str:
        """ returns current BTC price in USDT """
        try:
            ticker = self._client.get_symbol_ticker(symbol="BTCUSDT")
            print("🐍 File: api/api.py | Line: 41 | get_btc_price ~ ticker",ticker)
            return ticker['price']
        except Exception as e:
            return f"Error fetching BTC price: {str(e)}"
    
    def get_exchange_limits(self, use_testnet: bool = False) -> str:
        """ returns current BTC price in USDT """
        api_url = "https://api.binance.com/api"
        limits_endpoint = "/v3/exchangeInfo"

        limits_url = api_url + limits_endpoint

        try:
            # ticker = self._client.
            print("🐍 File: api/api.py | Line: 41 | get_btc_price ~ ticker",ticker)
            return ticker['price']
        except Exception as e:
            return f"Error fetching BTC price: {str(e)}"
