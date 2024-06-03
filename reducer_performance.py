import sys
from datetime import datetime


def read_input(file):
    for line in file:
        yield line.strip().split("\t")


def main():
    current_symbol = None
    first_price = None
    data = read_input(sys.stdin)

    for fields in data:
        stock_symbol, date, closing_price = fields
        closing_price = float(closing_price)
        date = datetime.strptime(date, "%Y-%m-%d")

        if current_symbol == stock_symbol:
            if first_price is None:
                first_price = closing_price
            performance = (closing_price - first_price) / first_price
            print(f"{stock_symbol}\t{date}\t{performance}")
        else:
            current_symbol = stock_symbol
            first_price = closing_price


if __name__ == "__main__":
    main()
