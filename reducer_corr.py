import sys
from datetime import datetime
import numpy as np


def read_input(file):
    for line in file:
        yield line.strip().split("\t")


def main():
    gold_prices = []
    silver_prices = []
    data = read_input(sys.stdin)

    for fields in data:
        stock_symbol, date, closing_price = fields
        closing_price = float(closing_price)
        date = datetime.strptime(date, "%Y-%m-%d")

        if stock_symbol == "GOLDBEES":
            gold_prices.append(closing_price)
        elif stock_symbol == "SILVERBEES":
            silver_prices.append(closing_price)

    if len(gold_prices) == len(silver_prices):
        correlation = np.corrcoef(gold_prices, silver_prices)[0, 1]
        print(f"Correlation between Gold BEES and Silver BEES: {correlation}")


if __name__ == "__main__":
    main()
