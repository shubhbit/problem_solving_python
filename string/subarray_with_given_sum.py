def subarray_with_given_sum(array, summation):
    index = -1
    for i in range(len(array)):
        for j in range(i+1,len(array)+1):
            if sum(array[i:j]) == summation:
                index = [i+1, j]
                break
        if index != -1:
            break
    return index

def main():
    ar = [1,2,3,7,5]
    print(subarray_with_given_sum(ar, 10))

if __name__ == "__main__":
    main()
