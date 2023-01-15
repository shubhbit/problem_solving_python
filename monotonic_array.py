# write a python function to check whether an array of integers is monotonic
# or not

# if it is either monotone increasing or monotone decreasing.

# ar = [1, 3, 7, 8]
# out: True

# ar = [3,5,2,10]
# out: False

def is_monotonic(array):
    monotonic = True
    comp_map = {"positive": 0, "negative": 0}
    for index in range(len(array) - 1):
        if array[index+1] - array[index] > 0:
            if comp_map["negative"] > 0:
                monotonic = False
                break
            comp_map["positive"] += 1
        elif array[index+1] - array[index] < 0:
            if comp_map["positive"] > 0:
                monotonic = False
                break
            comp_map["negative"] += 1
            
    return monotonic


if __name__ == "__main__":
    print(is_monotonic([1, 3, 7, 8]))
    print(is_monotonic([3, 5, 2, 10]))
    print(is_monotonic([6, 5, 4, 4]))
    print(is_monotonic([5, 15, 20, 10]))
