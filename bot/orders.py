from bot.client import BinanceClient
from bot.validators import validate_order_inputs
from bot.logging_config import setup_logger

logger = setup_logger()

def place_order(symbol, side, order_type, quantity, price=None):
    validate_order_inputs(symbol, side, order_type, quantity, price)

    client = BinanceClient()
    response = client.place_order(symbol, side, order_type, quantity, price)

    logger.info(
        "Order successful | orderId=%s status=%s executedQty=%s avgPrice=%s",
        response.get("orderId"), response.get("status"),
        response.get("executedQty"), response.get("avgPrice")
    )

    return {
        "orderId":     response.get("orderId"),
        "status":      response.get("status"),
        "executedQty": response.get("executedQty"),
        "avgPrice":    response.get("avgPrice")
    }