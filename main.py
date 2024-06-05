<<<<<<< HEAD
import os
import subprocess
import sys
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
        return

    # Run the reducer
    reducer_process = subprocess.Popen(
        [sys.executable, reducer_script], stdin=subprocess.PIPE, stdout=subprocess.PIPE
    )
    reducer_output, reducer_error = reducer_process.communicate(input=mapper_output)

    if reducer_error:
        print(f"Reducer error: {reducer_error.decode()}")
        return

    return reducer_output.decode()


def main():
    # Define input files and stock symbols
    input_files = {
        "NIFTY50.csv": "NIFTY50",
        "GOLDBEES.csv": "GOLDBEES",
        "SILVERBEES.csv": "SILVERBEES",
    }

    # Define mapper and reducer scripts
    mapper_scripts = {
        "volatility_analysis": "mapper_volatility.py",
    }

    reducer_scripts = {
        "volatility_analysis": "reducer_volatility.py",
    }

    """ mapper_scripts = {
        "moving_averages": "mapper_ma.py",
        "daily_returns": "mapper_returns.py",
        "correlation_analysis": "mapper_corr.py",
        "volatility_analysis": "mapper_volatility.py",
        "performance_comparison": "mapper_performance.py",
    }

    reducer_scripts = {
        "moving_averages": "reducer_ma.py",
        "daily_returns": "reducer_returns.py",
        "correlation_analysis": "reducer_corr.py",
        "volatility_analysis": "reducer_volatility.py",
        "performance_comparison": "reducer_performance.py",
    }
 """
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
                print(output)

            print(f"Completed {analysis} for {stock_symbol} using {file_name}")


if __name__ == "__main__":
    main()
=======
import os
import subprocess
import sys
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
        return

    # Run the reducer
    reducer_process = subprocess.Popen(
        [sys.executable, reducer_script], stdin=subprocess.PIPE, stdout=subprocess.PIPE
    )
    reducer_output, reducer_error = reducer_process.communicate(input=mapper_output)

    if reducer_error:
        print(f"Reducer error: {reducer_error.decode()}")
        return

    return reducer_output.decode()


def main():
    # Define input files and stock symbols
    input_files = {
        "NIFTY50.csv": "NIFTY50",
        "GOLDBEES.csv": "GOLDBEES",
        "SILVERBEES.csv": "SILVERBEES",
    }

    # Define mapper and reducer scripts
    mapper_scripts = {
        "moving_averages": "mapper_ma.py",
        "daily_returns": "mapper_returns.py",
        "correlation_analysis": "mapper_corr.py",
        "volatility_analysis": "mapper_volatility.py",
        "performance_comparison": "mapper_performance.py",
    }

    reducer_scripts = {
        "moving_averages": "reducer_ma.py",
        "daily_returns": "reducer_returns.py",
        "correlation_analysis": "reducer_corr.py",
        "volatility_analysis": "reducer_volatility.py",
        "performance_comparison": "reducer_performance.py",
    }

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
                print(output)

            print(f"Completed {analysis} for {stock_symbol} using {file_name}")


if __name__ == "__main__":
    main()
>>>>>>> 7a42576e1897d86858dfb56149328bc36ac5ec04
