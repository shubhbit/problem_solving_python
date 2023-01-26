def remove_duplicates(st):
    char_frequency = {}
    st = list(st)
    for indx, i in enumerate(st):
        if i not in char_frequency:
            char_frequency[i] = 1
        else:
            st.pop(indx)
    print("after removing duplicates: {}".format("".join(st)))

if __name__ == "__main__":
    st = "zvvo"
    remove_duplicates(st)
    st = "gfg"
    remove_duplicates(st)