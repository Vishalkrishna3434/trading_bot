# Trading Bot — Binance Futures Testnet

A Python CLI application to place Market and Limit orders on Binance Futures Testnet (USDT-M).

---

## Project Structure
```
trading_bot/
  bot/
    __init__.py          # Package marker
    client.py            # Binance API client wrapper
    orders.py            # Order placement logic
    validators.py        # Input validation
    logging_config.py    # Logging setup
  logs/
    trading_bot.log      # Generated log file
  cli.py                 # CLI entry point
  .env                   # API credentials (not committed)
  requirements.txt
  README.md
```

---

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/Vishalkrishna3434/trading_bot
cd trading_bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file in the root directory
```
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

Get your API credentials from: https://testnet.binancefuture.com

---

## How to Run

### Place a MARKET order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Place a LIMIT order
```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 42000
```

### CLI arguments

| Argument | Required | Description |
|---|---|---|
| `--symbol` | Yes | Trading pair e.g. `BTCUSDT` |
| `--side` | Yes | `BUY` or `SELL` |
| `--type` | Yes | `MARKET` or `LIMIT` |
| `--quantity` | Yes | Order quantity e.g. `0.01` |
| `--price` | LIMIT only | Limit price e.g. `42000` |

---

## Example Output
```
--- Order Request ---
  Symbol     : BTCUSDT
  Side       : BUY
  Order Type : MARKET
  Quantity   : 0.01
  Price      : N/A (MARKET order)
---------------------

--- Order Response ---
  Order ID     : 12879950416
  Status       : NEW
  Executed Qty : 0.000
  Avg Price    : 0.00
----------------------
✅ Order placed successfully!
```

---

## Logging

All API requests, responses, and errors are logged to `logs/trading_bot.log`.
```
2026-03-19 19:03:26,368 | INFO | Input validation passed | symbol=BTCUSDT side=BUY type=MARKET qty=0.01 price=None
2026-03-19 19:03:27,179 | INFO | Connected to Binance Futures Testnet
2026-03-19 19:03:27,179 | INFO | Placing order | symbol=BTCUSDT side=BUY type=MARKET qty=0.01 price=None
2026-03-19 19:03:27,993 | INFO | Order placed | orderId=12879950416 status=NEW
```

---

## Assumptions

- All orders are placed on **Binance Futures Testnet (USDT-M)** — no real funds involved
- LIMIT orders use `timeInForce=GTC` (Good Till Cancelled) by default
- `status=NEW` on testnet is expected — testnet has low liquidity so orders may not fill immediately
- API credentials must be testnet credentials, not live Binance credentials

---

## Requirements
```
python-binance
python-dotenv
```