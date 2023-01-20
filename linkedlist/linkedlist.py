from node import Node


def create_list(data):
    head = Node()
    copy = head
    for val in data:
        print("adding element {} to linkedlist".format(val))
        copy.set_value(val)
        copy.next = Node()
        copy = copy.next
    return head


def traverse_list(head):
    print("Traversing linkedlist..")
    while head.next != None:
        print(head.value)
        head = head.next


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
    head = create_list(data)
    traverse_list(head)
    find_duplicates_in_list(head)
