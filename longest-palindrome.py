def longest_palindrome_simple(st):
    palindrome = None
    for i in range(len(st)):
        for j in range(i+1, len(st)+1):
            if st[i:j] == st[i:j][::-1]:
                if not palindrome or len(st[i:j]) > len(palindrome):
                    palindrome = st[i:j]


    print(palindrome)

                        
if __name__ == "__main__":
    st = "aaaabbaa"
    longest_palindrome_simple(st)
    st = "abc"
    longest_palindrome_simple(st)

