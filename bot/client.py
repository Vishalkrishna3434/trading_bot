from binance.client import Client
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv
import os
from bot.logging_config import setup_logger

logger = setup_logger()
load_dotenv()

class BinanceClient:

    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise EnvironmentError(
                "BINANCE_API_KEY or BINANCE_API_SECRET not found. Check your .env file."
            )

        self.client = Client(api_key, api_secret, testnet=True)
        logger.info("Connected to Binance Futures Testnet")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        logger.info(
            "Placing order | symbol=%s side=%s type=%s qty=%s price=%s",
            symbol, side, order_type, quantity, price
        )

        try:
            if order_type == "MARKET":
                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )
            elif order_type == "LIMIT":
                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )

            logger.info(
                "Order placed | orderId=%s status=%s",
                response.get("orderId"), response.get("status")
            )
            return response

        except BinanceAPIException as e:
            logger.error(
                "Binance API error | code=%s message=%s",
                e.code, e.message
            )
            raise