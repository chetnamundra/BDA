<<<<<<< HEAD
#!/usr/bin/env python3
import sys
import csv


def read_input(file):
    for line in file:
        yield line.strip().split(",")


def main():
    for file_path in sys.argv[1:]:
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header line
            for fields in reader:
                try:
                    date = fields[0]
                    stock_symbol = file_path.split(".")[
                        0
                    ]  # Use the file name as the stock symbol
                    closing_price = float(
                        fields[4]
                    )  # Assuming the closing price is in the 5th column
                    print(f"{stock_symbol}\t{closing_price}")
                except IndexError:
                    continue  # Skip lines that don't have enough fields
                except ValueError:
                    continue  # Skip lines with non-numeric closing price


if __name__ == "__main__":
    main()
=======
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
>>>>>>> 7a42576e1897d86858dfb56149328bc36ac5ec04
