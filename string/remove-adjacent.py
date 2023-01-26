def remove_adjacent(st):
    st = list(st)
    for indx, i in enumerate(st):
        count = 1
        for j in st[indx+1:]:
            if i == j:             
                count += 1
            else:
                break
        if count> 1:
            del st[indx:indx+count] 


    print("removed: ", "".join(st))


if __name__ == "__main__":
    st = "randomneeeesfoork"
    remove_adjacent(st)
