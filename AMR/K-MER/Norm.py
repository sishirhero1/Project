import pandas as pd
from scipy.stats import zscore

# Load the TSV file into a DataFrame
file_path = "/mnt/d/Projects/Abhishek_sir_project/AMR/Results/merged_output7.tsv"
df = pd.read_csv(file_path, sep='\t')

# Normalize each row by dividing by the sum of the specified columns
cols_to_normalize = df.columns[1:17]  # Columns 2 to 17
df[cols_to_normalize] = df[cols_to_normalize].div(df[cols_to_normalize].sum(axis=1), axis=0)

# Apply Z-score standardization
#df[cols_to_normalize] = df[cols_to_normalize].apply(zscore)
df[cols_to_normalize] = df[cols_to_normalize].apply(zscore, axis=1)

# Save the modified DataFrame to a new TSV file
output_file_path = "/mnt/d/Projects/Abhishek_sir_project/AMR/Results/merged_output7_norm.tsv"
df.to_csv(output_file_path, sep='\t', index=False)

print(f"Processed file saved to {output_file_path}")

