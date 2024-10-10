from random import choice
from random import seed
import textwrap

# Set seed for reproducability.
seed(123)

# 1. Generate a random DNA sequence of 1 million base pairs (using A, C, G, T).

## Create random DNA sequence of length 1000000.
DNA = ""
for count in range(1000000):
    DNA += choice("CGTA")

# 2. Format the sequence with 80 base pairs per line.

DNA_wrapped = textwrap.wrap(DNA, width = 80)

# 3. Save the sequence in FASTA format in the "data" directory, with the filename "random_sequence.fasta".

if __name__ == "__main__":
    try:
        with open('/Users/iriskim/Desktop/05-first-exam-irisk2050/bioinformatics_project/data/random_sequence.fasta', 'a') as f:
            f.write(f">Random DNA sequence of length 1000000\n")
            f.write(DNA_wrapped)
        print(f"Successfully saved random DNA sequence to random_sequence.fasta.")
    except OSError:
        print("An OSError occurred!")