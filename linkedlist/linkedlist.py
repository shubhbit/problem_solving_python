from node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None
    def create_list(self, data):
        for index, val in enumerate(data):
            print("adding element {} to linkedlist".format(val))
            if index == 0:
                self.head = Node(val)
                copy = self.head
            copy.next = Node(val)
            copy = copy.next

    def traverse_list(self):
        print("Traversing linkedlist..")
        copy = self.head
        while copy.next != None:
            print(copy.value)
            copy = copy.next
        print(copy.value)
