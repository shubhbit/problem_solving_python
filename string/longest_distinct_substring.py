def longest_distinct_substring(st):
    longest = ""
    for i in  range(len(st)):
        for j in range(i+1, len(st)+1):
            sub = st[i:j]
            if len(sub) == len(set(sub)):

                if len(sub) > len(longest):
                    longest = sub
    print("longest unique substring: {}".format(len(longest)))


if __name__ == "__main__":
    longest_distinct_substring("geeksforgeeks")