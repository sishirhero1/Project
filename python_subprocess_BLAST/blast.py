import os
import subprocess
import csv

# ...
outfmt = '10 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore'
def run_blast(input_file, output_file, blast_result):
    blast_program = 'blastp'
    
    cmd = [
        blast_program,
        '-query', input_file,
        '-db', blast_result,
        '-outfmt', outfmt,
        '-out', output_file
    ]

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()

    stderr_output = process.stderr.read().decode('utf-8')
    if process.returncode != 0:
        print(f"Error running BLAST: {stderr_output}")
    else:
        print(f"BLAST completed successfully. Results saved in {output_file}")

# ...

# ...

def process_single_fasta():
    fasta_path = input("Enter the path to the single fasta file: ")
    output_path = input("Enter the output CSV file path: ")
    database_name = "/mnt/c/Users/DELL/OneDrive/Desktop/Abhishek_sir_project/python_subprocess_BLAST/sbdb/spdb"
    # Ensure the output path is a complete file path, not just a directory
    if not output_path.endswith('.csv'):
        output_path = os.path.join(output_path, 'output.csv')

    run_blast(fasta_path, output_path, database_name)

# ...

# ...

def process_multiple_fasta():
    directory_path = input("Enter the path to the directory containing multiple fasta files: ")
    output_directory = input("Enter the output directory path: ")
    database_name = "/mnt/c/Users/DELL/OneDrive/Desktop/Abhishek_sir_project/python_subprocess_BLAST/sbdb/spdb"

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    print(f"Files in the directory: {os.listdir(directory_path)}")

    for filename in os.listdir(directory_path):
        if filename.endswith(".fasta"):
            fasta_path = os.path.join(directory_path, filename)
            output_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_results.csv")

            run_blast(fasta_path, output_path, database_name)

# ...

def main():
    choice = input("Choose an option:\n1. Single Fasta File\n2. Multiple Fasta Files\nEnter 1 or 2: ")

    if choice == "1":
        process_single_fasta()
    elif choice == "2":
        process_multiple_fasta()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
