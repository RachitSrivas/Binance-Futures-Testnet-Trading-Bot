# 📈 Binance Futures Testnet Trading Bot

A lightweight, robust Python application for placing orders on the Binance Futures Testnet (USDT-M). Built with clean architecture, this bot features comprehensive error handling, real-time logging, and dual interfaces (Interactive CLI and Desktop GUI).

---

## 🚀 How to Run the Bot

Once you have completed the setup steps below, you can launch the bot using either of these two commands from your terminal:

### 1️⃣ Run the Interactive Terminal (CLI Mode)
Provides a fast, step-by-step guided menu right inside your command line.

python cli.py
2️⃣ Run the Desktop App (GUI Mode)
Launches a native window with dropdowns, dynamic inputs, and a visual output log.

Bash
python gui.py
✨ Key Features
Multi-Order Support: Execute MARKET, LIMIT, and STOP (Stop-Limit) orders for both BUY and SELL sides.

Dual Interfaces: Choose between a dynamic CLI or a lightweight Tkinter GUI.

Bulletproof Validation: Prevents bad API calls by strictly validating quantities, required prices, and order types before sending.

Comprehensive Logging: Records all session activity, API successes, and error codes to a persistent bot_activity.log file.

Secure Environment: Uses a .env file to ensure API keys are never hardcoded into the project.

⚙️ Setup & Installation
1. Prerequisites
Python 3.8+ installed.

A Binance Futures Testnet account.

An API Key and Secret Key generated from testnet.binancefuture.com. (Important: Ensure you check the "Enable Futures" permission when creating the key).

2. Environment Setup
Clone the repository and open your terminal inside the project folder. Create and activate a virtual environment:

For Windows:

Bash
python -m venv venv
.\venv\Scripts\activate
For Mac/Linux:

Bash
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Install the required libraries (python-binance and python-dotenv):

Bash
pip install -r requirements.txt
4. Add Your API Keys
Create a new file named exactly .env in the root folder of the project. Add your keys like this (no quotes, no spaces):

Code snippet
BINANCE_TESTNET_API_KEY=your_actual_api_key_here
BINANCE_TESTNET_API_SECRET=your_actual_api_secret_here
📁 Project Architecture
Plaintext
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py           # Handles Binance API authentication
│   ├── orders.py           # Core logic for executing trades
│   ├── validators.py       # Pre-flight checks for user inputs
│   └── logging_config.py   # Configures console and file log streams
├── .env                    # Hidden file for API credentials
├── cli.py                  # Entry Point: Terminal Interface
├── gui.py                  # Entry Point: Desktop UI Interface
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
📌 Important Notes
Testnet Only: This bot is strictly configured to hit the testnet.binancefuture.com endpoints. It will not work with Mainnet keys, and it will reject Spot Testnet keys.

Logs: Check the bot_activity.log file to view a detailed history of your API requests and Binance server responses.
