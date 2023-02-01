
def push(x, st1, st2):
    st2.append(x)

def pop(st1, st2):
    popped_element = -1
    if st2:
        for i in range(len(st2)):
            st1.append(st2.pop())
        popped_element = st1.pop()
        for i in range(len(st1)):
            st2.append(st1.pop())
    return popped_element

if __name__ == "__main__":
    print("INPUT: ")
    num_test_cases =  int(input())
    tests = list(map(int, input().split(" ")))
    st1 = []
    st2 = []
    indx = 0
    print("OUTPUT: ")
    while indx < len(tests):
        if tests[indx] == 1:
            push(tests[indx+1], st1, st2)
            indx += 2
        else:
            print(pop(st1, st2), end=" ")
            indx += 1
