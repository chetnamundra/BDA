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
