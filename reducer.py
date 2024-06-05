<<<<<<< HEAD
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
            num_records = int(fields[2])
            if current_symbol == stock_symbol:
                total_closing_price += closing_price
                count += num_records
            else:
                if current_symbol:
                    average = total_closing_price / count
                    print(f"{current_symbol}\t{average}")
                current_symbol = stock_symbol
                total_closing_price = closing_price
                count = num_records
        except ValueError:
            continue  # Skip lines with non-numeric values

    if current_symbol == stock_symbol:
        average = total_closing_price / count
        print(f"{current_symbol}\t{average}")


if __name__ == "__main__":
    main()
=======
import sys


def read_input():
    for line in sys.stdin:
        yield line.strip().split("\t")


def reducer():
    current_symbol = None
    total_closing_price = 0
    count = 0

    data = read_input()
    for fields in data:
        try:
            stock_symbol = fields[0]
            closing_price = float(fields[1])
            if current_symbol == stock_symbol:
                total_closing_price += closing_price
                count += 1
            else:
                if current_symbol:
                    average = total_closing_price / count
                    print(f"{current_symbol}\t{average}")
                current_symbol = stock_symbol
                total_closing_price = closing_price
                count = 1
        except ValueError:
            continue  # Skip lines with non-numeric closing price

    if current_symbol == stock_symbol:
        average = total_closing_price / count
        print(f"{current_symbol}\t{average}")


if __name__ == "__main__":
    reducer()
>>>>>>> 7a42576e1897d86858dfb56149328bc36ac5ec04
