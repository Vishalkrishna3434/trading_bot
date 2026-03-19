import logging
import os

def setup_logger():
    # Prevent adding duplicate handlers if setup_logger() is called more than once
    logger = logging.getLogger("trading_bot")
    if logger.handlers:
        return logger
    
    logger.setLevel(logging.DEBUG)

    # Ensure logs directory exists before creating file handler
    os.makedirs("logs", exist_ok=True)

    file_handler = logging.FileHandler("logs/trading_bot.log")
    file_handler.setLevel(logging.DEBUG)  # Capture everything in file for debugging

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Show only important messages to user

    # Include timestamp, level, and message — minimum viable log format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger