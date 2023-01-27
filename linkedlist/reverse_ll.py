from linkedlist import LinkedList

# 1->2->3->4->5->6


def reverse_list(head):
    print("reversing linked list..")
    prev = None
    count = 0
    while head.next != None:
        temp = head
        head = head.next
        if count == 0:
            prev = temp
            prev.next = None
        else:
            temp.next = prev
            prev = temp
        count += 1
    head.next = prev
    return head


if __name__ == "__main__":
    data = [1, 34, 23, 98, 1, 29, 3]
    linked_list = LinkedList()
    linked_list.create_list(data)
    linked_list.traverse_list()
    head = reverse_list(linked_list.head)
    linked_list.head = head
    linked_list.traverse_list()
