from node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.current = None

    def create_list(self, data):
        for index, val in enumerate(data):
            print("adding element {} to linked-list".format(val))
            node = Node(val)
            if index == 0:
                self.head = node                
            else:
                self.current.next = node
            self.current = node


    def traverse_list(self):
        print("Traversing linkedlist..")
        copy = self.head
        while copy.next != None:
            print(copy.value)
            copy = copy.next
        print(copy.value)
