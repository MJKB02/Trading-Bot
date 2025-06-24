from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

class BasicBot:
    def __init__(self, testnet=True):
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == "MARKET":
                return self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=quantity
                )
            elif order_type == "LIMIT":
                return self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="LIMIT",
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )
            else:
                raise ValueError("❌ Unsupported order type.")
        except Exception as e:
            print("❌ Error placing order:", e)
            return None
