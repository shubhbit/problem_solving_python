# Inversion Count: For an array, inversion count indicates how far (or close) the array is
# from being sorted. If array is already sorted then the inversion count is 0.
# If an array is sorted in the reverse order then the inversion count is the maximum.
# Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

def find_inversion_count(ar):
    inversion_count = 0
    for indx, item in enumerate(ar):
        for item2 in ar[indx+1:]:
            if item > item2:
                inversion_count += 1
    print("inversion count: ", inversion_count)


if __name__ == "__main__":
    ar = [2, 4, 1, 3, 5]
    find_inversion_count(ar)
    ar = [2, 3, 4, 5, 6]
    find_inversion_count(ar)
    ar = [10, 10, 10]
    find_inversion_count(ar)
