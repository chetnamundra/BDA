import subprocess


def run_command(command, input_data=None):
    result = subprocess.run(command, input=input_data, text=True, capture_output=True)
    return result.stdout


# Define the file paths for the CSV files
csv_files = ["NIFTY50.csv", "GOLDBEES.csv", "SILVERBEES.csv"]

# Step 1: Run Mapper
mapper_output = ""
for file in csv_files:
    with open(file, "r") as f:
        mapper_output += run_command(["python", "mapper.py", file], f.read())

# Step 2: Run Combiner
combiner_output = run_command(["python", "combiner.py"], mapper_output)

# Step 3: Run Reducer
reducer_output = run_command(["python", "reducer.py"], combiner_output)

# Print the final output
print(reducer_output)
