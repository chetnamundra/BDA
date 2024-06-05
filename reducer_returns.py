<<<<<<< HEAD
import sys
from datetime import datetime


def read_input(file):
    for line in file:
        yield line.strip().split("\t")


def main():
    current_symbol = None
    prev_close = None
    data = read_input(sys.stdin)

    for fields in data:
        stock_symbol, date, closing_price = fields
        closing_price = float(closing_price)
        date = datetime.strptime(date, "%Y-%m-%d")

        if current_symbol == stock_symbol:
            if prev_close is not None:
                daily_return = (closing_price - prev_close) / prev_close
                print(f"{stock_symbol}\t{date}\t{daily_return}")
            prev_close = closing_price
        else:
            current_symbol = stock_symbol
            prev_close = closing_price


if __name__ == "__main__":
    main()
=======
import sys
from datetime import datetime


def read_input(file):
    for line in file:
        yield line.strip().split("\t")


def main():
    current_symbol = None
    prev_close = None
    data = read_input(sys.stdin)

    for fields in data:
        stock_symbol, date, closing_price = fields
        closing_price = float(closing_price)
        date = datetime.strptime(date, "%Y-%m-%d")

        if current_symbol == stock_symbol:
            if prev_close is not None:
                daily_return = (closing_price - prev_close) / prev_close
                print(f"{stock_symbol}\t{date}\t{daily_return}")
            prev_close = closing_price
        else:
            current_symbol = stock_symbol
            prev_close = closing_price


if __name__ == "__main__":
    main()
>>>>>>> 7a42576e1897d86858dfb56149328bc36ac5ec04
