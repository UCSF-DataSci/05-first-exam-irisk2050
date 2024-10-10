import os
import argparse

# 2. Implement the following functions:
#    - `complement(sequence)`: Returns the complement of a DNA sequence (A -> T, C -> G, G -> C, T -> A).

def complement(sequence):
    ## Make DNA sequence all upper case.
    sequence = sequence.upper()

    ## Mapping table.
    dna_base = "ACGT"
    dna_complement = "TGCA"

    ## Create and return the complement sequence using the mapping table.
    my_mapping_table = str.maketrans(dna_base, dna_complement)
    complement = sequence.translate(my_mapping_table)

    return complement

# 2. Implement the following functions:
#     - `reverse(sequence)`: Returns the reverse of a sequence (e.g. "CCTCAGC" -> "CAGCCTC").

def reverse(sequence):
    return sequence[::-1]

# 2. Implement the following functions:
#    - `reverse_complement(sequence)`: Returns the reverse complement of a DNA sequence (e.g. "CCTCAGC" -> "GAGCTTG"); i.e. the reverse of the complement (apply `complement` then `reverse`, or vice versa).

def reverse_complement(sequence):
    dna_complement = complement(sequence)
    return reverse(dna_complement)

# 3. For the input sequence, print:
#    - The original sequence
#    - Its complement
#    - Its reverse
#    - Its reverse complement

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform various operations on DNA sequences.")

    # 1. Accept a DNA sequence as a command-line argument.

    parser.add_argument("--dna_sequence", "-dna", type = str, help = "Input DNA sequence.")

    args = parser.parse_args()
    dna_seq = args.dna_sequence

    # 3. For the input sequence, print:
    #    - The original sequence
    #    - Its complement
    #    - Its reverse
    #    - Its reverse complement

    print(f"Original sequence: {dna_seq}")
    print(f"Complement: {complement(dna_seq)}")
    print(f"Reverse: {reverse(dna_seq)}")
    print(f"Reverse complement: {reverse_complement(dna_seq)}")