<<<<<<< HEAD
import sys
import numpy as np
from datetime import datetime


def read_input(file):
    for line in file:
        yield line.strip().split("\t")


def main():
    current_symbol = None
    prices = []
    data = read_input(sys.stdin)

    for fields in data:
        stock_symbol, date, closing_price = fields
        closing_price = float(closing_price)
        date = datetime.strptime(date, "%Y-%m-%d")

        if current_symbol == stock_symbol:
            prices.append(closing_price)
        else:
            if current_symbol:
                volatility = np.std(prices) * np.sqrt(252)
                print(f"{current_symbol}\t{volatility}")
            current_symbol = stock_symbol
            prices = [closing_price]

    if current_symbol == stock_symbol:
        volatility = np.std(prices) * np.sqrt(252)
        print(f"{current_symbol}\t{volatility}")


if __name__ == "__main__":
    main()
=======
import sys
import numpy as np
from datetime import datetime


def read_input(file):
    for line in file:
        yield line.strip().split("\t")


def main():
    current_symbol = None
    prices = []
    data = read_input(sys.stdin)

    for fields in data:
        stock_symbol, date, closing_price = fields
        closing_price = float(closing_price)
        date = datetime.strptime(date, "%Y-%m-%d")

        if current_symbol == stock_symbol:
            prices.append(closing_price)
        else:
            if current_symbol:
                volatility = np.std(prices) * np.sqrt(252)
                print(f"{current_symbol}\t{volatility}")
            current_symbol = stock_symbol
            prices = [closing_price]

    if current_symbol == stock_symbol:
        volatility = np.std(prices) * np.sqrt(252)
        print(f"{current_symbol}\t{volatility}")


if __name__ == "__main__":
    main()
>>>>>>> 7a42576e1897d86858dfb56149328bc36ac5ec04
