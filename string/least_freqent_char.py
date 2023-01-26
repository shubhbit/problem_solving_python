# Python – Least Frequent Character in String

def least_frequent(st):
    least = st[0]
    for i in st:
        if st.count(i) < st.count(least):
            least = i
    print("least frequent char in string : {0} is {1}".format(st, least))

if __name__ == "__main__":
    least_frequent("shubham")
    least_frequent("pandey")
    least_frequent("allahabad")