def longest_unique_substring(st):
    longest = ""
    for i in range(0, len(st)):
        for j in range(i+1, len(st)+1):
            if len(st[i:j]) == len(set(st[i:j])):
                if len(st[i:j]) > len(longest):
                    longest = st[i:j]
    return longest

if __name__ == "__main__":
    print(longest_unique_substring('abcabcbb')) # abc
    print(longest_unique_substring('bbbbb')) # b
    print(longest_unique_substring('pwwkew')) # wke
