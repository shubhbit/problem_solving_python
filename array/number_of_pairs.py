# Given two arrays X and Y of positive integers,
# find the number of pairs such that x**y > y**x (raised to power of)
# where x is an element from X and y is an element from Y.

def find_pairs(ar1, ar2):
    count = 0
    for x in ar1:
        for y in ar2:
            if x**y > y**x:
                count += 1
    print("no. of pairs: ", count)


if __name__ == "__main__":
    M = [2, 1, 6]
    N = [1, 5]
    find_pairs(M, N)
    M = [2, 3, 4, 5]
    N = [1, 2, 3]
    find_pairs(M, N)
