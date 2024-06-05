import yfinance as yf
import pandas as pd

# Define the stock symbols for Nifty 50, Gold BEES, and Silver BEES
stocks = {
    "NIFTY50": "^NSEI",  # Nifty 50 Index
    "GOLDBEES": "GOLDBEES.NS",
    "SILVERBEES": "SILVERBEES.NS",
}

# Define the period for historical data
start_date = "2023-01-01"
end_date = "2024-01-01"

for stock_name, stock_symbol in stocks.items():
    # Download historical data
    data = yf.download(stock_symbol, start=start_date, end=end_date)

    # Save to CSV
    data.to_csv(f"{stock_name}.csv")

print("Data downloaded and saved as CSV files.")
