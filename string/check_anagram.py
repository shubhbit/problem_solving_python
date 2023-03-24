# Anagram: two strings are anagram if they are having same characters with same
# frequency not necessarily in same order.

def is_anagram(a, b):
    is_anagram = True
    if len(a) == len(b):
        for i in set(a):
            if a.count(i) != b.count(i):
                is_anagram = False
                break
    else:
        is_anagram = False
    if is_anagram:
        print("{0} and {1} are anagram".format(a, b))
    else:
        print("{0} and {1} not are anagram".format(a, b))


if __name__ == "__main__":
    a = "geeksforgeeks"
    b = "forgeeksgeeks"
    is_anagram(a, b)
    a = "allergy"
    b = "allergic"
    is_anagram(a, b)
    
