import argparse
import re

# 3. Find all occurrences of the cut site (specified below) in the DNA sequence.

def find_cutsites(dna_seq, cutsite_seq):
    ## Change to uppercase and remove the "|" to get the clean cut site sequence
    cutsite_seq_clean = cutsite_seq.upper().replace("|", "")
    
    ## Get the index of the cut site indicator "|" in the cut site sequence
    cutsite_index = cutsite_seq.index("|")

    ## Use regex to find all matches of the cut site sequence in the DNA sequence
    cutsite_loc = [m.start() + cutsite_index for m in re.finditer(cutsite_seq_clean, dna_seq.upper())]

    return cutsite_loc

# 4. Find all pairs of cut site locations that are 80,000-120,000 base pairs (80-120 kbp) apart.

def find_cutsite_pairs(cutsite_loc):
    return [[i, i + 1] for i in range(len(cutsite_loc) - 1)
            if 80000 <= (cutsite_loc[i + 1] - cutsite_loc[i]) <= 120000]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Finds all instances of cut sites in DNA sequence.")

    # 1. Accept two arguments: the FASTA file path (data/random_sequence.fasta) and a cut site sequence (e.g., "G|GATCC")

    parser.add_argument("--input_file", "-i", type=str, help="Input fasta file containing DNA sequence.")
    parser.add_argument("--cutsite_seq", "-c", type=str, help="Cut site sequence.")

    args = parser.parse_args()
    input_file = args.input_file
    cutsite_seq = args.cutsite_seq

    try:
        with open(input_file, 'r') as f:
            ## Skip the first line description since it's not part of the DNA sequence.
            next(f)

            # 2. Read the FASTA file and save the DNA sequence to a variable omitting whitespace.

            dna_seq = f.read().replace(" ", "").replace("\n", "")

            cutsite_loc = find_cutsites(dna_seq, cutsite_seq)
            cutsite_pairs = find_cutsite_pairs(cutsite_loc)

            # 5. Print the total number of cut site pairs found and the positions of the first 5 pairs.

            print(f"Analyzing cut site: {cutsite_seq}")
            print(f"Total cut sites found: {len(cutsite_loc)}")
            print(f"Total cut site pairs 80-120 kbp apart: {len(cutsite_pairs)}")
            print("First 5 cut site pairs:")
            for pair in cutsite_pairs[:5]:
                print(pair)

        # 6. Save a summary of the results in the results directory as "distant_cutsite_summary.txt".

        summary_file = "/Users/iriskim/Desktop/05-first-exam-irisk2050/bioinformatics_project/results/distant_cutsite_summary.txt"
        with open(summary_file, "w") as f2:
            f2.write(f"Analyzing cut site: {cutsite_seq}\n")
            f2.write(f"Total cut sites found: {len(cutsite_loc)}\n")
            f2.write(f"Total cut site pairs 80-120 kbp apart: {len(cutsite_pairs)}\n")
            f2.write("First 5 cut site pairs:\n")
            for pair in cutsite_pairs[:5]:
                f2.write(f"{pair}\n")
            print(f"Results saved to {summary_file}")

    except OSError as e:
        print(f"An OSError occurred: {e}")