import os
import subprocess
import sys
import matplotlib.pyplot as plt
from io import StringIO


def run_mapper_reducer(mapper_script, reducer_script, input_file, stock_symbol):
    with open(input_file, "r") as f:
        mapper_input = f.read()

    # Run the mapper
    mapper_process = subprocess.Popen(
        [sys.executable, mapper_script, stock_symbol],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    mapper_output, mapper_error = mapper_process.communicate(
        input=mapper_input.encode()
    )

    if mapper_error:
        print(f"Mapper error: {mapper_error.decode()}")
        return None

    # Run the reducer
    reducer_process = subprocess.Popen(
        [sys.executable, reducer_script], stdin=subprocess.PIPE, stdout=subprocess.PIPE
    )
    reducer_output, reducer_error = reducer_process.communicate(input=mapper_output)

    if reducer_error:
        print(f"Reducer error: {reducer_error.decode()}")
        return None

    return reducer_output.decode()


def main(plot_graph=True):
    # Define input files and stock symbols
    input_files = {
        "NIFTY50.csv": "NIFTY50",
        "GOLDBEES.csv": "GOLDBEES",
        "SILVERBEES.csv": "SILVERBEES",
    }

    # Define mapper and reducer scripts
    mapper_scripts = {
        "moving_averages": "mapper_ma.py",
    }

    reducer_scripts = {
        "moving_averages": "reducer_ma.py",
    }

    # Prepare data storage
    results = {}

    # Run each analysis for each input file
    for file_name, stock_symbol in input_files.items():
        print(f"Running analysis for {stock_symbol} using {file_name}...")

        for analysis, mapper_script in mapper_scripts.items():
            reducer_script = reducer_scripts[analysis]

            # Simulate MapReduce job
            output = run_mapper_reducer(
                mapper_script, reducer_script, file_name, stock_symbol
            )

            if output:
                # Store the results
                if stock_symbol not in results:
                    results[stock_symbol] = []

                for line in output.splitlines():
                    if line:
                        fields = line.strip().split("\t")
                        results[stock_symbol].append((fields[1], float(fields[2])))

                print(f"Completed {analysis} for {stock_symbol} using {file_name}")

        # Plot the results
    if plot_graph:
        for stock_symbol, data in results.items():
            dates = [entry[0] for entry in data]
            averages = [entry[1] for entry in data]

            plt.figure(figsize=(10, 5))
            plt.plot(averages, color="b")
            plt.title(f"Moving Average for {stock_symbol}")
            plt.xlabel("Time")
            plt.ylabel("Moving Average")
            plt.tight_layout()
            plt.show()


if __name__ == "__main__":
    main()
