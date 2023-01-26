def rearrange_sorted_array(ar):
    index = 0
    while index < len(ar):
        if len(ar[index:]) > 1:
            max_item = max(ar[index:])
            min_item = min(ar[index:])
            indx_max = ar.index(max_item)
            indx_min = ar.index(min_item)
            ar.pop(indx_max)
            ar.pop(indx_min)
            ar.insert(index, max_item)
            ar.insert(index+1, min_item)
        index = index+2

    print(ar)

if __name__ == "__main__":
    ar = [1,2,3,4,5,6]
    rearrange_sorted_array(ar)
    ar = [10,20,30,40,50,60,70,80,90,100,110]
    rearrange_sorted_array(ar)