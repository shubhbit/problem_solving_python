def find_missing(ar):
    count = len(ar)
    for i in range(1, count+1):
        if i not in ar:
            return i

if __name__ == "__main__":
    ar = {1,2,3,5}
    print(find_missing(ar))
    ar = {6,1,2,8,3,4,7,10,5}
    print(find_missing(ar))