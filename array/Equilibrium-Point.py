def equilibrium_point(ar):
    eq_point = 0
    for index in range(len(ar)):
        if sum(ar[:index]) == sum(ar[index+1:]):
            eq_point = index+1
    print("equilibrium_point: ", eq_point)


if __name__ == "__main__":
    ar = [1, 3, 5, 2, 2]
    equilibrium_point(ar)
    ar = [1]
    equilibrium_point(ar)