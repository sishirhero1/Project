from flask import Flask, render_template, request, redirect
import os
import subprocess
import pandas as pd


app = Flask(__name__)
outfmt = '10 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore'
database_name = "/mnt/d/Projects/Abhishek_sir_project/python_subprocess_BLAST/sbdb/spdb"

def run_blast(input_file, output_file):
    blast_program = 'blastp'
    
    cmd = [
        blast_program,
        '-query', input_file,
        '-db', database_name,
        '-outfmt', outfmt,
        '-out', output_file
    ]

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()

    stderr_output = process.stderr.read().decode('utf-8')
    if process.returncode != 0:
        return f"Error running BLAST: {stderr_output}"
    else:
        return None

def process_results(output_file):
    df = pd.read_csv(output_file, sep=',', header=None, names=['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore'])
    return df.to_dict(orient='records')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_single', methods=['POST'])
def upload_single():
    fasta_file = request.files['fasta_file']
    if fasta_file and fasta_file.filename.endswith('.fasta'):
        input_file = os.path.join('uploads', 'single.fasta')
        fasta_file.save(input_file)

        output_file = os.path.join('results', 'single_result.csv')
        error_message = run_blast(input_file, output_file)

        if error_message:
            return render_template('error.html', message=error_message)

        results = process_results(output_file)
        fasta_filename = os.path.basename(input_file)
        return render_template('result_single.html', results=results)
    else:
        return render_template('error.html', message='Invalid file format. Please upload a .fasta file.')

@app.route('/upload_multiple', methods=['POST'])
def upload_multiple():
    fasta_files = request.files.getlist('fasta_files')
    input_files = []

    for i, fasta_file in enumerate(fasta_files):
        if fasta_file.filename.endswith('.fasta'):
            input_file = os.path.join('uploads', f'multiple_{i + 1}.fasta')
            fasta_file.save(input_file)
            input_files.append(input_file)

    output_files = [os.path.join('results', f'multiple_result_{i + 1}.csv') for i in range(len(input_files))]

    for input_file, output_file in zip(input_files, output_files):
        error_message = run_blast(input_file, output_file)
        

        if error_message:
            return render_template('error.html', message=error_message)

    results = [process_results(output_file) for output_file in output_files]
    return render_template('result_multiple.html', results=results)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('results', exist_ok=True)
    app.run(debug=True)