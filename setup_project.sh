# Set current directory to x.
cd /Users/iriskim/Desktop/05-first-exam-irisk2050

# 1. Create the main project directory called "bioinformatics_project".
mkdir -p bioinformatics_project

# 2. Inside the main directory, create the following subdirectories: data, scripts, results.
mkdir -p bioinformatics_project/data
mkdir -p bioinformatics_project/scripts
mkdir -p bioinformatics_project/results

# 3. In the scripts directory, create empty Python files:
touch bioinformatics_project/scripts/generate_fasta.py
touch bioinformatics_project/scripts/dna_operations.py
touch bioinformatics_project/scripts/find_cutsites.py

# 4. In the results directory, create an empty file named "cutsite_summary.txt".
touch bioinformatics_project/results/cutsite_summary.txt

# 5. In the data directory, create an empty file named "random_sequence.fasta".
touch bioinformatics_project/data/random_sequence.fasta

# 6. Create a README.md file in the main project directory with a brief description of the project structure.
echo "# Bioinformatics Project" > bioinformatics_project/README.md
echo "## Directory Structure" >> bioinformatics_project/README.md
echo "- data: contains raw and processed data files" >> bioinformatics_project/README.md
echo "- scripts: contains project scripts" >> bioinformatics_project/README.md
echo "- results: stores output of analyses and summaries" >> bioinformatics_project/README.md
