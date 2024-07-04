# String Compression: Compress a string by replacing 
# repeated characters with a single character and a count.
# Input: "aabcccccaaa"
# Output: "a2b1c5a3"

# Input: "abcdef"
# Output: "a1b1c1d1e1f1" (no compression possible, since all characters are unique)

# Input: "aaabbbbcccaaaa"
# Output: "a3b4c3a4"

def compress_string(text):
    count = 1
    prev = text[0]
    compressed_st = ""
    for index in range(1, len(text)):
        if text[index] == prev:
            count += 1
        else:
            compressed_st += prev + str(count)
            count = 1
        prev = text[index]
    compressed_st += prev + str(count)
    return compressed_st

if __name__ == "__main__":
    print(compress_string('aabcccccaaa'))
    print(compress_string('abcdef'))
    print(compress_string('aaabbbbcccaaaa'))

