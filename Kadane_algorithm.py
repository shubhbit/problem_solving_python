def find_contiguous_subarray_max_sum(ar):
    max_sum = [ar[0]]
    count = len(ar)
    for i in range(count):
        for j in range(i+1, count+1):
            if sum(ar[i:j]) > sum(max_sum):
                max_sum = ar[i:j]
    return max_sum

if __name__ == "__main__":
    ar = [1,2,3,-2,5]
    print(find_contiguous_subarray_max_sum(ar))
    ar = [-1,-2,-3,-4]
    print(find_contiguous_subarray_max_sum(ar))