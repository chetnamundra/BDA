#!/usr/bin/env python3
import sys


def read_input(file):
    for line in file:
        yield line.strip().split("\t")


def main():
    current_symbol = None
    total_closing_price = 0
    count = 0

    data = read_input(sys.stdin)
    for fields in data:
        try:
            stock_symbol = fields[0]
            closing_price = float(fields[1])
            if current_symbol == stock_symbol:
                total_closing_price += closing_price
                count += 1
            else:
                if current_symbol:
                    print(f"{current_symbol}\t{total_closing_price}\t{count}")
                current_symbol = stock_symbol
                total_closing_price = closing_price
                count = 1
        except ValueError:
            continue  # Skip lines with non-numeric closing price

    if current_symbol == stock_symbol:
        print(f"{current_symbol}\t{total_closing_price}\t{count}")


if __name__ == "__main__":
    main()
