
def next_greater(ar):
    st = ""
    for indx, i in enumerate(ar):
        for j in ar[indx+1:]:
            if j > i:
                st += str(j)
                break
    st += "-1"
    return " ".join(list(st))



if __name__ == "__main__":
    # Input: 
    # N = 4, arr[] = [1 3 2 4]
    # Output:
    # 3 4 4 -1
    ar = [1, 3, 2, 4]
    print(next_greater(ar))
