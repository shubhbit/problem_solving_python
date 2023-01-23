def reverse_words(st):
    rev_st = ""
    print(" ".join(st.split(" ")[::-1]))

if __name__ == "__main__":
    st = "I like this program very much"
    reverse_words(st)