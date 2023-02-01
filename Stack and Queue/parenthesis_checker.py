from stack import Stack

op_cl_map = {"{":"}", "(":")", "[":"]"}

def parenthesis_balanced(st):
    new_stack = Stack()
    is_balanced = True
    for bracket in st:
        if bracket in op_cl_map:
            new_stack.push(bracket)
        else:
            popped = new_stack.pop()
            if op_cl_map[popped] != bracket:
                is_balanced = False
                break
    if new_stack.stack:
        is_balanced = False
    return is_balanced

if __name__ == "__main__":
    sts = ["{[({})]}",  "{[(})]}"]
    for st in sts:
        print("{} is balanced".format(st)) if parenthesis_balanced(st) else print("{} is not balanced".format(st)) 
