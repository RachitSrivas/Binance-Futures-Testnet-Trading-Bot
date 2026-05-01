def validate_order_inputs(symbol: str, side: str, order_type: str, quantity: float, price: float = None, stop_price: float = None):
    valid_sides = ['BUY', 'SELL']
    valid_types = ['MARKET', 'LIMIT', 'STOP']

    if side.upper() not in valid_sides:
        raise ValueError(f"Invalid side: {side}. Must be BUY or SELL.")
    
    if order_type.upper() not in valid_types:
        raise ValueError(f"Invalid order type: {order_type}. Must be MARKET, LIMIT, or STOP.")
    
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")
    
    if order_type.upper() == 'LIMIT' and (price is None or price <= 0):
        raise ValueError("A valid price greater than 0 is required for LIMIT orders.")
        
    if order_type.upper() == 'STOP':
        if price is None or price <= 0:
            raise ValueError("A valid execution price is required for STOP (Stop-Limit) orders.")
        if stop_price is None or stop_price <= 0:
            raise ValueError("A valid stop_price is required for STOP (Stop-Limit) orders.")
            
    return True