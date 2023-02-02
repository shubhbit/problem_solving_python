class Stack:
    def __init__(self):
        self.st = []

    def push(self, x):
        self.st.append(x)

    def pop(self):
        popped = self.st.pop()
        return popped

    def find_min(self):
        copy = self.st
        min = copy.pop()
        while True:
            try:
                el = copy.pop()
                if el < min:
                    min = el
            except Exception as e:
                break

        return min

    def traverse_stack(self):
        for i in self.st:
            print(i, end="->")

if __name__ == "__main__":
    stack = Stack()
    for i in [32,12,45,87,10, -1, 90]:
        stack.push(i)
    stack.traverse_stack()
    print("\n min: ",stack.find_min())