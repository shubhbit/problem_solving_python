# write a python function to check whether a string is symmetrical and palindrome
# Symmetrical: if two halves of string are same
# palindrome: if two halves of string are reverse to each other

def symmetric_palindrome(st):
    sym = False
    pal = False
    half_string_len = len(st) //2
    first_half = st[:half_string_len]
    second_half = st[half_string_len:]
    if first_half == second_half:
        sym = True
    if first_half == second_half[::-1]:
        pal = True
    print("string{0}=> is symmetrical: {1}\nstring is palindrome: {2}".format(st, sym, pal))

if __name__ == "__main__":
    symmetric_palindrome("khokho")
    symmetric_palindrome("amaama")
