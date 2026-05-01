from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot.logging_config import logger
from bot.client import get_binance_client

def place_order(symbol: str, side: str, order_type: str, quantity: float, price: float = None, stop_price: float = None):
    client = get_binance_client()
    
    logger.info(f"Preparing {order_type} {side} order for {quantity} {symbol}")
    
    try:
        if order_type.upper() == 'MARKET':
            response = client.futures_create_order(
                symbol=symbol.upper(), side=side.upper(), type='MARKET', quantity=quantity
            )
        elif order_type.upper() == 'LIMIT':
            response = client.futures_create_order(
                symbol=symbol.upper(), side=side.upper(), type='LIMIT', 
                timeInForce='GTC', quantity=quantity, price=price
            )
        elif order_type.upper() == 'STOP':
            # STOP in Binance Futures is a Stop-Limit order
            response = client.futures_create_order(
                symbol=symbol.upper(), side=side.upper(), type='STOP', 
                timeInForce='GTC', quantity=quantity, price=price, stopPrice=stop_price
            )
        
        logger.info(f"Order Success! Order ID: {response.get('orderId')}")
        logger.debug(f"Full response: {response}")
        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: Status Code {e.status_code} - {e.message}")
        return {"error": e.message}
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return {"error": str(e)}