from linkedlist import LinkedList


def find_duplicates_in_list(head):
    unique = []
    while head.next != None:
        if head.value not in unique:
            unique.append(head.value)
        else:
            print("{} is duplicate".format(head.value))
        head = head.next


if __name__ == "__main__":
    data = [1, 34, 23, 98, 1, 29, 3]
    linked_list = LinkedList()
    linked_list.create_list(data)
    linked_list.traverse_list()
    find_duplicates_in_list(linked_list.head)
