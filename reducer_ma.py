import sys
from collections import deque
from datetime import datetime

window_size = 50  # Moving average window size


def read_input(file):
    for line in file:
        yield line.strip().split("\t")


def main():
    current_symbol = None
    prices = deque()
    data = read_input(sys.stdin)

    for fields in data:
        stock_symbol, date, closing_price = fields
        closing_price = float(closing_price)
        date = datetime.strptime(date, "%Y-%m-%d")

        if current_symbol == stock_symbol:
            prices.append(closing_price)
            if len(prices) > window_size:
                prices.popleft()
            if len(prices) == window_size:
                moving_average = sum(prices) / window_size
                print(f"{stock_symbol}\t{date}\t{moving_average}")
        else:
            current_symbol = stock_symbol
            prices = deque([closing_price])


if __name__ == "__main__":
    main()
