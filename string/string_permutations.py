
def find_permutations(st, i , length):
    if i == length:
        results.append("".join(st))
    else:
        for j in range(i, length):
            st[i], st[j] = st[j], st[i]
            find_permutations(st, i+1, length)
            st[i], st[j] = st[j], st[i]
    
if __name__ == "__main__":
    results = []
    st = "ABC"
    find_permutations(list(st), 0, len(st))
    print("perms: ", results)
    results = []
    st = "ABSG"
    find_permutations(list(st), 0, len(st))
    print("perms: ", results)
