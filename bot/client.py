import os
from binance.client import Client
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv
from bot.logging_config import logger

load_dotenv()

def get_binance_client():
    api_key = os.getenv("BINANCE_TESTNET_API_KEY")
    api_secret = os.getenv("BINANCE_TESTNET_API_SECRET")

    if not api_key or not api_secret:
        logger.error("API keys missing. Please check your .env file.")
        raise ValueError("Missing Binance API credentials.")

    try:
        # testnet=True automatically routes to https://testnet.binancefuture.com for futures
        client = Client(api_key, api_secret, testnet=True)
        logger.debug("Binance client successfully initialized.")
        return client
    except Exception as e:
        logger.error(f"Failed to initialize Binance client: {e}")
        raise