import argparse
from bot.orders import place_order
from bot.logging_config import setup_logger

logger = setup_logger()

def parse_args():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol",     required=True,  help="Trading pair e.g. BTCUSDT")
    parser.add_argument("--side",       required=True,  choices=["BUY", "SELL"], help="BUY or SELL")
    parser.add_argument("--type", required=True,  choices=["MARKET", "LIMIT"], help="MARKET or LIMIT")
    parser.add_argument("--quantity",   required=True,  type=float, help="Order quantity e.g. 0.01")
    parser.add_argument("--price",      required=False, type=float, help="Price (required for LIMIT orders)")

    return parser.parse_args()


def main():
    args = parse_args()

    # Print order request summary
    print("\n--- Order Request ---")
    print(f"  Symbol     : {args.symbol}")
    print(f"  Side       : {args.side}")
    print(f"  Order Type : {args.order_type}")
    print(f"  Quantity   : {args.quantity}")
    print(f"  Price      : {args.price if args.price else 'N/A (MARKET order)'}")
    print("---------------------\n")

    try:
        result = place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.order_type,
            quantity=args.quantity,
            price=args.price
        )

        # Print order response
        print("--- Order Response ---")
        print(f"  Order ID     : {result.get('orderId')}")
        print(f"  Status       : {result.get('status')}")
        print(f"  Executed Qty : {result.get('executedQty')}")
        print(f"  Avg Price    : {result.get('avgPrice')}")
        print("----------------------")
        print("Order placed successfully!\n")

    except ValueError as e:
        print(f"\n Validation error: {e}\n")
        logger.error("Validation error | %s", e)

    except EnvironmentError as e:
        print(f"\n Environment error: {e}\n")
        logger.error("Environment error | %s", e)

    except Exception as e:
        print(f"\n Order failed: {e}\n")
        logger.error("Unexpected error | %s", e)


if __name__ == "__main__":
    main()