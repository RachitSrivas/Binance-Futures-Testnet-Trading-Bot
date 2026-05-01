import sys
import time
from bot.validators import validate_order_inputs
from bot.orders import place_order
from bot.logging_config import logger

def clear_screen():
    print("\n" * 50) # simple cross-platform way to push text up

def main_menu():
    while True:
        print("\n" + "="*40)
        print(" 🤖 BINANCE FUTURES TESTNET BOT")
        print("="*40)
        print("1. Place MARKET Order")
        print("2. Place LIMIT Order")
        print("3. Place STOP-LIMIT Order")
        print("4. Exit")
        print("="*40)
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '4':
            print("\nExiting bot. Goodbye! 👋")
            sys.exit(0)
            
        if choice not in ['1', '2', '3']:
            print("❌ Invalid choice. Please select 1, 2, 3, or 4.")
            time.sleep(1)
            continue
            
        handle_order_flow(choice)

def handle_order_flow(choice):
    print("\n--- Let's build your order ---")
    try:
        symbol = input("Enter Symbol (e.g., BTCUSDT): ").upper().strip()
        side = input("Enter Side (BUY/SELL): ").upper().strip()
        qty = float(input("Enter Quantity (e.g., 0.01): ").strip())
        
        price = None
        stop_price = None
        order_type = "MARKET"

        if choice == '2':
            order_type = "LIMIT"
            price = float(input("Enter Target Price: ").strip())
            
        elif choice == '3':
            order_type = "STOP"
            stop_price = float(input("Enter Trigger Stop Price: ").strip())
            price = float(input("Enter Execution Limit Price: ").strip())

        # Validate everything before sending to Binance
        validate_order_inputs(symbol, side, order_type, qty, price, stop_price)
        
        print("\n⏳ Sending order to Binance Testnet...")
        response = place_order(symbol, side, order_type, qty, price, stop_price)

        if response and "error" not in response:
            print("\n✅ SUCCESS! Order Placed.")
            print(f"➜ Order ID: {response.get('orderId')}")
            print(f"➜ Status:   {response.get('status')}")
        else:
            print(f"\n❌ FAILURE: {response.get('error', 'Check logs for details.')}")

    except ValueError as e:
        print(f"\n❌ Input Error: {e}")
        logger.error(f"User Input Error: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")
        
    input("\nPress ENTER to return to the main menu...")

if __name__ == "__main__":
    main_menu()