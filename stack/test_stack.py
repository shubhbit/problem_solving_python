from stack import Stack

if __name__ == "__main__":
    stack = Stack()
    l = [2,43,1,9,5]
    for i in l:
        stack.push(i)

    stack.print_stack()
    while len(stack.stack) != 0:
        print("popped item: ", stack.pop())