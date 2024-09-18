import pandas as pd

# Load the metadata and output TSV files with appropriate delimiters
metadata = pd.read_csv("/mnt/d/Projects/Abhishek_sir_project/AMR/metadata_new.csv")
output = pd.read_csv("/mnt/d/Projects/Abhishek_sir_project/AMR/Results/output7.tsv", sep="\t")

# Remove the '.ffn' part from the 'Genome' column in output
output['Genome'] = output['Genome'].str.replace('.ffn', '')

# Convert the data type of the "Genome" column in metadata to object
metadata['Genome'] = metadata['Genome'].astype(str)

# Merge metadata with output based on "Genome" column
merged_data = pd.merge(output, metadata, on="Genome")


# Save the merged data to a new TSV file
merged_data.to_csv("/mnt/d/Projects/Abhishek_sir_project/AMR/Results/merged_output7.tsv", sep="\t", index=False)