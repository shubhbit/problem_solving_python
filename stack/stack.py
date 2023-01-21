class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        item = self.stack.pop()
        return item

    def print_stack(self):
        for i in self.stack[::-1]:
            print(i)

            