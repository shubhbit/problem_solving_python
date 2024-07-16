# The Repeated DNA Sequences problem involves finding 
# all the 10-letter-long sequences (substrings) that 
# occur more than once in a given DNA string. 
# DNA sequences are composed of the characters 'A', 'C', 'G', 
# and 'T'.

# Problem Statement
# Given a string s that represents a DNA sequence, 
# find all the 10-letter-long sequences (substrings) 
# that occur more than once in the DNA molecule.

# Example
# Input: "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]
# Example 4:
# Input: "ATATATATATATATATATAT"
# Output: ["ATATATATAT", "TATATATATA"]

def repeated_dna_sequence(dna):
    repeated_subsequence = {}
    for i in range(0, len(dna)):
        for j in range(i+1, len(dna)+1):
            sub_str = dna[i:j]
            if len(sub_str) == 10:
                if sub_str in repeated_subsequence:
                    repeated_subsequence[sub_str] += 1
                else:
                    repeated_subsequence[sub_str] = 1
    return [sequence for sequence in repeated_subsequence if repeated_subsequence[sequence] > 1]

if __name__ == "__main__":
    print(repeated_dna_sequence('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
    print(repeated_dna_sequence('ATATATATATATATATATAT'))
