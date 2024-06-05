import subprocess
import pandas as pd
from scipy.stats import pearsonr

# List of files to process
files = ["GOLDBEES.csv", "SILVERBEES.csv"]


# Function to execute the mapper_corr.py for each file
def process_file(file):
    # Use subprocess to simulate Hadoop streaming
    with open(file, "r") as f:
        # Assuming mapper_corr.py is in the current directory
        proc = subprocess.Popen(
            ["python", "mapper_corr.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE
        )
        stdout, _ = proc.communicate(f.read().encode())
        proc.wait()
        return stdout.decode().strip()


# Execute for each file and gather data
data = {}
for file in files:
    data[file] = process_file(file)

# Prepare data for correlation calculation
gold_data = []
silver_data = []

for file, content in data.items():
    lines = content.split("\n")
    for line in lines:
        if line.strip():
            fields = line.split("\t")
            if file == "GOLDBEES.csv":
                gold_data.append(fields)
            elif file == "SILVERBEES.csv":
                silver_data.append(fields)

# Convert to dataframes
gold_df = pd.DataFrame(gold_data, columns=["Date", "Gold Closing Price"])
silver_df = pd.DataFrame(silver_data, columns=["Date", "Silver Closing Price"])

# Merge on Date
merged_data = pd.merge(gold_df, silver_df, on="Date")

# Convert columns to numeric
merged_data["Gold Closing Price"] = pd.to_numeric(merged_data["Gold Closing Price"])
merged_data["Silver Closing Price"] = pd.to_numeric(merged_data["Silver Closing Price"])

# Calculate correlation
correlation, _ = pearsonr(
    merged_data["Gold Closing Price"], merged_data["Silver Closing Price"]
)

# Print correlation
print(f"Correlation between Gold BEES and Silver BEES: {correlation:.4f}")
