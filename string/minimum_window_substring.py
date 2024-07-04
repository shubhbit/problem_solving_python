# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"

# Input: s = "a", t = "a"
# Output: "a"

# Input: s = "a", t = "aa"
# Output: ""
# 1. identify all the substrings
# 2. whether substring contains all characters of second string

def minimum_window_substring(st, check):
    min_win = ""
    for i in range(0, len(st)):
        for j in range(i+1, len(st)+1):
            sub_str = st[i:j]
            if False not in [False for ch in check if check.count(ch)!=sub_str.count(ch)]:
                if len(sub_str) < len(min_win) or len(min_win) == 0:
                    min_win = sub_str
    return min_win

if __name__ == "__main__":
    print(minimum_window_substring("ADOBECODEBANC", "ABC"))
    print(minimum_window_substring("a", "a"))
    print(minimum_window_substring("a", "aa"))