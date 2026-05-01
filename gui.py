import tkinter as tk
from tkinter import ttk, messagebox
from bot.validators import validate_order_inputs
from bot.orders import place_order

class TradingBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Binance Testnet Trading Bot")
        self.root.geometry("450x550")
        self.root.configure(padx=20, pady=20)

        # Title
        ttk.Label(root, text="🤖 Trading Bot UI", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Frame for all our inputs
        input_frame = ttk.Frame(root)
        input_frame.pack(fill="x", pady=10)

        # 1. Symbol Input
        ttk.Label(input_frame, text="Symbol:").grid(row=0, column=0, sticky="w", pady=5)
        self.symbol_var = tk.StringVar(value="BTCUSDT")
        ttk.Entry(input_frame, textvariable=self.symbol_var).grid(row=0, column=1, sticky="ew", pady=5, padx=5)

        # 2. Side Dropdown
        ttk.Label(input_frame, text="Side:").grid(row=1, column=0, sticky="w", pady=5)
        self.side_var = tk.StringVar(value="BUY")
        ttk.Combobox(input_frame, textvariable=self.side_var, values=["BUY", "SELL"], state="readonly").grid(row=1, column=1, sticky="ew", pady=5, padx=5)

        # 3. Order Type Dropdown
        ttk.Label(input_frame, text="Order Type:").grid(row=2, column=0, sticky="w", pady=5)
        self.type_var = tk.StringVar(value="MARKET")
        type_cb = ttk.Combobox(input_frame, textvariable=self.type_var, values=["MARKET", "LIMIT", "STOP"], state="readonly")
        type_cb.grid(row=2, column=1, sticky="ew", pady=5, padx=5)
        type_cb.bind("<<ComboboxSelected>>", self.toggle_fields) # Triggers function when changed

        # 4. Quantity Input
        ttk.Label(input_frame, text="Quantity:").grid(row=3, column=0, sticky="w", pady=5)
        self.qty_var = tk.StringVar(value="0.01")
        ttk.Entry(input_frame, textvariable=self.qty_var).grid(row=3, column=1, sticky="ew", pady=5, padx=5)

        # 5. Target Price Input (Disabled by default)
        ttk.Label(input_frame, text="Limit Price:").grid(row=4, column=0, sticky="w", pady=5)
        self.price_var = tk.StringVar()
        self.price_entry = ttk.Entry(input_frame, textvariable=self.price_var, state="disabled")
        self.price_entry.grid(row=4, column=1, sticky="ew", pady=5, padx=5)

        # 6. Stop Price Input (Disabled by default)
        ttk.Label(input_frame, text="Stop Price:").grid(row=5, column=0, sticky="w", pady=5)
        self.stop_price_var = tk.StringVar()
        self.stop_price_entry = ttk.Entry(input_frame, textvariable=self.stop_price_var, state="disabled")
        self.stop_price_entry.grid(row=5, column=1, sticky="ew", pady=5, padx=5)

        # Submit Button
        ttk.Button(root, text="Place Order", command=self.submit_order).pack(pady=15, fill="x")

        # Output Box (To show success/failure messages)
        ttk.Label(root, text="Output Log:").pack(anchor="w")
        self.log_text = tk.Text(root, height=8, state="disabled", bg="#f0f0f0")
        self.log_text.pack(fill="both", expand=True)

    # Automatically disables/enables boxes based on order type
    def toggle_fields(self, event=None):
        order_type = self.type_var.get()
        if order_type == "MARKET":
            self.price_entry.config(state="disabled")
            self.stop_price_entry.config(state="disabled")
        elif order_type == "LIMIT":
            self.price_entry.config(state="normal")
            self.stop_price_entry.config(state="disabled")
        elif order_type == "STOP":
            self.price_entry.config(state="normal")
            self.stop_price_entry.config(state="normal")

    # Helper function to print to our UI box
    def log_message(self, msg):
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, msg + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")

    # The main execution function
    def submit_order(self):
        symbol = self.symbol_var.get().upper().strip()
        side = self.side_var.get().upper().strip()
        order_type = self.type_var.get().upper().strip()
        
        try:
            qty = float(self.qty_var.get() or 0)
            price = float(self.price_var.get()) if self.price_var.get() else None
            stop_price = float(self.stop_price_var.get()) if self.stop_price_var.get() else None
            
            # Use our existing validator
            validate_order_inputs(symbol, side, order_type, qty, price, stop_price)
            
            self.log_message(f"⏳ Sending {order_type} {side} order...")
            
            # Use our existing order logic
            response = place_order(symbol, side, order_type, qty, price, stop_price)
            
            if response and "error" not in response:
                self.log_message(f"✅ SUCCESS! Order ID: {response.get('orderId')}\n")
            else:
                self.log_message(f"❌ ERROR: {response.get('error', 'Check logs.')}\n")
                
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("System Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = TradingBotGUI(root)
    root.mainloop()