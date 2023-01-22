def leaders_in_an_array(ar):
    leaders = []
    for index, i in enumerate(ar):
        if_leader = True
        for j in ar[index+1:]:
            if not i >= j:
                if_leader = False
                break
        if if_leader:
            leaders.append(i)
    print("leaders: {}".format(leaders))


if __name__ == "__main__":
    ar = [16, 17, 4, 3, 5, 2]
    leaders_in_an_array(ar)
    ar = [1, 2, 3, 4, 0]
    leaders_in_an_array(ar)
