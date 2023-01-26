# without using any extra space.

def merge_sorted_array(ar1, ar2):
    for i in arr1:
        for indx, j in enumerate(arr2):
            if i <= j:
                arr2.insert(indx, i)
                break

    return arr2





if __name__ == "__main__":
    arr1 = [1, 3, 5, 7]
    arr2 = [0, 2, 6, 8, 9]
    print(merge_sorted_array(arr1, arr2))
    arr1 = [10, 12] 
    arr2 = [5, 18, 20]
    print(merge_sorted_array(arr1, arr2))
