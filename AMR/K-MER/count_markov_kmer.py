import os
import numpy as np

def count_dinucleotides(sequence, order):
    counts = np.zeros((4, 4), dtype=int)
    for i in range(len(sequence) - order - 1):
        current_nucleotide = sequence[i]
        next_nucleotide = sequence[i + order + 1]
        if current_nucleotide in "ATGC" and next_nucleotide in "ATGC":
            current_index = "ATGC".index(current_nucleotide)
            next_index = "ATGC".index(next_nucleotide)
            counts[current_index][next_index] += 1
    return counts

def process_file(file_path, order):
    dinucleotide_counts = np.zeros((4, 4), dtype=int)
    with open(file_path, 'r') as f:
        current_gene = ""
        for line in f:
            if line.startswith(">"):
                if current_gene:
                    counts = count_dinucleotides(current_gene, order)
                    dinucleotide_counts += counts
                current_gene = ""
            else:
                current_gene += line.strip()
        if current_gene:
            counts = count_dinucleotides(current_gene, order)
            dinucleotide_counts += counts
    return dinucleotide_counts

def generate_output(input_directory, output_directory, order):
    files = [f for f in os.listdir(input_directory) if f.endswith(".ffn")]
    dinucleotide_matrix = []
    for file in files:
        file_path = os.path.join(input_directory, file)
        dinucleotide_counts = process_file(file_path, order)
        dinucleotide_matrix.append(dinucleotide_counts.flatten())
    dinucleotide_matrix = np.array(dinucleotide_matrix)
    dinucleotide_combinations = ["{}{}".format(a, b) for a in "ATGC" for b in "ATGC"]
    header = ["Genome"] + dinucleotide_combinations
    output_data = np.column_stack((files, dinucleotide_matrix))
    output_data = np.row_stack((header, output_data))

    output_file_path = os.path.join(output_directory, "output7.tsv")
    np.savetxt(output_file_path, output_data, delimiter="\t", fmt="%s")

def main():
    input_directory = input("Enter the input directory containing .ffn files: ")
    output_directory = input("Enter the output directory to save the .tsv file: ")
    order = int(input("Enter the Markov order (0 for 0th order, 1 for 1st order, etc.): "))
    generate_output(input_directory, output_directory, order)

if __name__ == "__main__":
    main()