import os
import pandas as pd
import itertools 

# Function to generate all possible 7-mers
def generate_7mers():
    nucleotides = ['A', 'C', 'G', 'T']
    return [''.join(n) for n in itertools.product(nucleotides, repeat=7)]

# Function to count 7-mers in a sequence
def count_7mers(sequence):
    counts = {}
    for i in range(len(sequence) - 6):
        kmer = sequence[i:i+7]
        counts[kmer] = counts.get(kmer, 0) + 1
    return counts

# Directory containing .ffn files
directory = "/mnt/d/Projects/Abhishek_sir_project/AMR/resistant"

# List to store file names
file_names = []

# Dictionary to store 7-mer counts for each file
data = {}

# Iterate through the directory
for filename in os.listdir(directory):
    if filename.endswith(".ffn"):
        file_names.append(filename)
        with open(os.path.join(directory, filename), 'r') as f:
            sequence = f.read()
            data[filename] = count_7mers(sequence)

# Generate all possible 7-mers
all_7mers = generate_7mers()

# Create a list of DataFrames for each file
dfs = []
for filename, counts in data.items():
    df = pd.DataFrame(counts.values(), index=counts.keys(), columns=[filename]).T
    dfs.append(df)

# Concatenate DataFrames along the columns axis
result_df = pd.concat(dfs)

# Fill missing values with 0 and reorder columns
result_df = result_df.reindex(columns=all_7mers, fill_value=0)

# Save DataFrame to a TSV file
result_df.to_csv("/mnt/d/Projects/Abhishek_sir_project/AMR/Results/7-mers.tsv", sep='\t')

