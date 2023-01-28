from node import Node


class Stack(object):
    def __init__(self):
        self.head = None
        self.current = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            self.current = self.head
        else:
            new_node = Node(data)
            self.current.next = new_node
            self.current = new_node
        print("pushed item: {} in stack".format(data))

# 1 -> 2 -> 3 -> 4 -> 5
# 1 -> none
    def pop(self):
        prev = self.head
        head = self.head
        if head is not None:
            while head:
                if head.next is None:
                    value = head.value
                    if head != prev:
                        prev.next = None
                    else:
                        self.head = None
                    print("\npopped element: {}".format(value))
                    return value
                prev = head
                head = head.next
        else:
            print("stack is empty")

    def traverse(self):
        print("traversing stack..")
        head = self.head
        if head:
            while head:
                print(head.value, end=" ")
                head = head.next
        else:
            print("stack is empty..")


if __name__ == "__main__":
    data = [1, 34, 23, 98, 1, 29, 3]
    stack = Stack()
    for item in data:
        stack.push(item)
    stack.traverse()
    while stack.head:
        stack.pop()
    stack.traverse()