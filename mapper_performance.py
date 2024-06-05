<<<<<<< HEAD
import sys
import csv


def read_input(file):
    for line in csv.reader(file):
        yield line


def main(stock_symbol):
    data = read_input(sys.stdin)
    for fields in data:
        try:
            if fields[0] == "Date":
                continue  # Skip the header line
            date = fields[0]
            closing_price = float(fields[4])
            print(f"{stock_symbol}\t{date}\t{closing_price}")
        except IndexError:
            continue
        except ValueError:
            continue


if __name__ == "__main__":
    stock_symbol = sys.argv[1]
    main(stock_symbol)
=======
import sys
import csv


def read_input(file):
    for line in csv.reader(file):
        yield line


def main(stock_symbol):
    data = read_input(sys.stdin)
    for fields in data:
        try:
            if fields[0] == "Date":
                continue  # Skip the header line
            date = fields[0]
            closing_price = float(fields[4])
            print(f"{stock_symbol}\t{date}\t{closing_price}")
        except IndexError:
            continue
        except ValueError:
            continue


if __name__ == "__main__":
    stock_symbol = sys.argv[1]
    main(stock_symbol)
>>>>>>> 7a42576e1897d86858dfb56149328bc36ac5ec04
