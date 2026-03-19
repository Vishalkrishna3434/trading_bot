from bot.logging_config import setup_logger

logger = setup_logger()

def validate_order_inputs(symbol, side, type, quantity, price):

    # 1. symbol must be a non-empty string of uppercase letters only
    if not isinstance(symbol, str) or len(symbol) == 0:
        raise ValueError(f"Invalid symbol: must be a non-empty string, got {repr(symbol)}")
    if not symbol.isupper():
        raise ValueError(f"Invalid symbol '{symbol}': must be uppercase letters only (e.g. 'BTCUSDT')")

    # 2. side must be BUY or SELL
    if side not in ("BUY", "SELL"):
        raise ValueError(f"Invalid side '{side}': must be 'BUY' or 'SELL'")

    # 3. order_type must be MARKET or LIMIT
    if type not in ("MARKET", "LIMIT"):
        raise ValueError(f"Invalid order_type '{type}': must be 'MARKET' or 'LIMIT'")

    # 4. quantity must be a positive number
    if not isinstance(quantity, (int, float)) or quantity <= 0:
        raise ValueError(f"Invalid quantity '{quantity}': must be a number greater than 0")

    # 5. price is required for LIMIT orders and must be positive
    if type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError(f"Invalid price '{price}': must be a number greater than 0 for LIMIT orders")

    logger.info(
        "Input validation passed | symbol=%s side=%s type=%s qty=%s price=%s",
        symbol, side, type, quantity, price
    )