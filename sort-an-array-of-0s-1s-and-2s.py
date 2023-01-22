# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

def sort_array(ar):
    sorted_ar = []
    for i in ar:
        if not sorted_ar:
            sorted_ar.append(i)
        else:
            inserted = False
            for index, j in enumerate(sorted_ar):
                if i <= j:
                    sorted_ar.insert(index, i)
                    inserted = True
                    break
            if not inserted:
                sorted_ar.append(i)

    print("sorted array: ", sorted_ar)


if __name__ == "__main__":
    ar = [0, 2, 1, 2, 0]
    sort_array(ar)
    ar = [0, 1, 0]
    sort_array(ar)
