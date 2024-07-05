# Isomorphic Strings
# Problem: Given two strings s and t, determine if they are 
# isomorphic. Two strings are isomorphic if the characters 
# in s can be replaced to get t.

# Example:

# Input: s = "egg", t = "add"
# Output: true

# Input: s = "foo", t = "bar"
# Output: false

def are_isomorphic(s, t):
    is_isomorphic = True
    ch_map = {}
    if len(s) == len(t):
        for indx, ch in enumerate(s):
            if ch not in ch_map:
                ch_map[ch] = t[indx]
            else:
                if ch_map[ch] != t[indx]:
                     is_isomorphic = False
                     break
    else:
        is_isomorphic = False
    return is_isomorphic

if __name__ == "__main__":
    print(are_isomorphic('egg', 'add'))
    print(are_isomorphic('foo', 'bar'))
    print(are_isomorphic('foo', 'hii'))


