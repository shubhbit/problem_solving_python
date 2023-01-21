
def count_triplet(ar):
    triplet_count = 0
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            if ar[i]+ar[j] in ar:
                triplet_count += 1
    return triplet_count

if __name__ == "__main__":
    ar = [1,5,3,2]
    print(count_triplet(ar))
    ar = [2,3,4]
    print(count_triplet(ar))
