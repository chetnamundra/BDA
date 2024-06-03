import csv
import sys


def read_input(file):
    for line in file:
        yield line.strip().split(",")


def mapper(stock_symbol, file_path):
    with open(file_path, "r") as file:
        data = read_input(file)
        for fields in data:
            try:
                if fields[0] == "Date":
                    continue  # Skip the header line
                date = fields[0]
                closing_price = float(
                    fields[4]
                )  # Assuming the closing price is in the 5th column
                print(f"{stock_symbol}\t{closing_price}")
            except IndexError:
                continue  # Skip lines that don't have enough fields
            except ValueError:
                continue  # Skip lines with non-numeric closing price


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: mapper.py <stock_symbol>")
        sys.exit(1)

    stock_symbol = sys.argv[1]
    file_path = f"{stock_symbol}.csv"
    mapper(stock_symbol, file_path)
