from node import Node


class Queue(object):
    def __init__(self):
        self.head = None
        self.current = None

    def queue(self, data):
        if self.head is None:
            self.head = Node(data)
            self.current = self.head
        else:
            new_node = Node(data)
            self.current.next = new_node
            self.current = new_node
        print("queued item: {} in queue".format(data))

# 1 -> 2 -> 3 -> 4 -> 5
# 1 -> none
    def dequeue(self):
        if self.head:
            popped = self.head
            self.head = self.head.next
            print("dequeued element: ", popped.value)
        else:
            print("Queue is empty")


    def traverse(self):
        print("traversing queue..")
        head = self.head
        if head:
            while head:
                print(head.value, end=" ")
                head = head.next
        else:
            print("queue is empty..")


if __name__ == "__main__":
    data = [1, 34, 23, 98, 1, 29, 3]
    queue = Queue()
    for item in data:
        queue.queue(item)
    queue.traverse()
    while queue.head:
        queue.dequeue()
    queue.traverse()