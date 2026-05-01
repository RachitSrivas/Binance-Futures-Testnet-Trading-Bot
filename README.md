# Binance Futures Testnet Trading Bot 🤖

A structured, robust, and user-friendly Python application that interacts with the Binance Futures Testnet (USDT-M) to place various types of trading orders. 

This project was built to demonstrate clean code architecture, API interaction, error handling, and enhanced user experiences via CLI and GUI interfaces.

---

## ✨ Features

### Core Requirements Fulfilled:
- **Order Types:** Successfully places `MARKET` and `LIMIT` orders for both `BUY` and `SELL` sides.
- **Structured Architecture:** Clear separation of concerns (API client, order logic, input validation, and user interface).
- **Robust Validation:** Prevents invalid inputs (e.g., negative quantities, missing prices for limit orders) before making API calls.
- **Comprehensive Logging:** Records all API requests, responses, and errors to both the console and a persistent `bot_activity.log` file.
- **Secure Credentials:** Utilizes `.env` variables to prevent hardcoding sensitive API keys.

### 🚀 Bonus Features Implemented:
1. **Third Order Type (`STOP-LIMIT`):** Added support for advanced Stop-Limit orders requiring both a trigger price and an execution price.
2. **Enhanced Interactive CLI:** Replaced basic command-line arguments with a user-friendly, step-by-step interactive terminal menu.
3. **Lightweight Desktop UI:** Built a native graphical user interface (GUI) using `tkinter` that dynamically adapts fields based on the selected order type.

---

## 📁 Project Structure

trading_bot/
│ 
├── bot/
│   ├── __init__.py
│   ├── client.py           # Initializes the Binance Testnet connection
│   ├── orders.py           # Core business logic for placing orders
│   ├── validators.py       # Validates user inputs before API execution
│   └── logging_config.py   # Configures console and file loggers
│
├── .env                    # (User-created) Stores API keys securely
├── cli.py                  # Entry point 1: Interactive Terminal Menu
├── gui.py                  # Entry point 2: Desktop Graphical Interface
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation

---

## ⚙️ Setup Instructions
1. Prerequisites
Python 3.x installed on your system.

A Binance Futures Testnet account with dummy USDT funds.

Generated API Key and Secret Key from testnet.binancefuture.com. (Ensure "Enable Futures" is checked on the API key).

2. Installation
Clone or extract the repository, open your terminal, and navigate to the project folder:

Bash
cd trading_bot
Create and activate a Python virtual environment:

Bash
# On Windows:
python -m venv venv
.\venv\Scripts\activate

# On Mac/Linux:
python3 -m venv venv
source venv/bin/activate
Install the required dependencies:

Bash
pip install -r requirements.txt
3. Environment Variables
Create a file named exactly .env in the root directory (next to cli.py). Add your Testnet API credentials to it:

Code snippet
BINANCE_TESTNET_API_KEY=your_api_key_here
BINANCE_TESTNET_API_SECRET=your_api_secret_here

---

## 💻 Usage Instructions
This bot offers two distinct ways to interact with the Binance Testnet:

Option A: The Interactive CLI Menu
Run the command line interface to be guided through a step-by-step terminal menu:

Bash
python cli.py
Follow the on-screen prompts to input your symbol (e.g., BTCUSDT), side, order type, quantity, and price.

Option B: The Desktop GUI
Run the graphical application for a point-and-click experience:

Bash
python gui.py
A window will appear allowing you to select your order parameters. The Limit and Stop price fields will automatically enable/disable based on your selected Order Type.

---

## 📝 Logging Details
All system activities, successful orders, and API errors are automatically tracked.

You can view real-time status updates in your terminal or the GUI output box.

A detailed, persistent history is saved to bot_activity.log in the root directory.

---

## 📌 Assumptions & Notes
This bot routes strictly to the USDT-M Futures Testnet (testnet.binancefuture.com). It will reject Spot Testnet keys.

Real funds are not used; this application requires testnet credentials.
