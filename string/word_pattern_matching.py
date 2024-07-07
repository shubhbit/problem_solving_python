# Word Pattern Matching: Given a pattern and a string str, 
# find if str follows the same pattern. Here, 
# "pattern" means a sequence of letters 
# (e.g., "abba") and "str" means a string 
# (e.g., "dog cat cat dog"). ==> True

# Input:
# Pattern = "abba"
# Str = "dog cat cat fish"
# Output: False

def word_pattern_matching(pattern, string):
    word = string.split(" ")
    word_map = {}
    is_matched = True
    if len(pattern) == len(word):
        for index, element in enumerate(pattern):
            if element not in word_map:
                word_map[element] = word[index]
            else:
                if word_map[element] != word[index]:
                    is_matched = False
                    break
    else:
        is_matched = False

    return is_matched


if __name__ == "__main__":
    print(word_pattern_matching('abba', 'dog cat cat dog'))
    print(word_pattern_matching('abba', 'dog cat cat fish'))