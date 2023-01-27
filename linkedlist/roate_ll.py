from linkedlist import LinkedList

# k = 3
# 1->2->3->4->5->6
# 4->5->6->1->2->3

def rotate_linked_list(head, k):
    count = 1
    copy = head
    temp = head
    while count <  k:
        copy = copy.next
        count += 1
    head = copy.next
    head_copy = head
    while head.next != None:
        head = head.next
    head.next = temp
    copy.next = None
    return head_copy


if __name__ == "__main__":
    data = [1, 34, 23, 98, 1, 29, 3]
    linked_list = LinkedList()
    linked_list.create_list(data)
    linked_list.traverse_list()
    head = rotate_linked_list(linked_list.head, 3)
    linked_list.head = head
    linked_list.traverse_list()

    data = {2, 4, 7, 8, 9}
    linked_list = LinkedList()
    linked_list.create_list(data)
    linked_list.traverse_list()
    head = rotate_linked_list(linked_list.head, 3)
    linked_list.head = head
    linked_list.traverse_list()
