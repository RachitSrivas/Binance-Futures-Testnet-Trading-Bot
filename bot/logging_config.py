import logging

def setup_logger():
    logger = logging.getLogger("TradingBot")
    logger.setLevel(logging.DEBUG)

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('bot_activity.log')
    
    c_handler.setLevel(logging.INFO) # Keep console clean
    f_handler.setLevel(logging.DEBUG) # Log everything to file

    # Create formatters
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(formatter)
    f_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger

logger = setup_logger()