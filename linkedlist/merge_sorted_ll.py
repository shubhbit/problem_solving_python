# Given two sorted linked lists consisting of N and M nodes respectively.
# The task is to merge both of the list (in-place) and return head of the merged list.


from linkedlist import LinkedList


def merge_sorted_ll(head1, head2):
    pass


if __name__ == "__main__":
    data = [34, 56, 78]
    linked_list1 = LinkedList()
    linked_list1.create_list(data)
    linked_list1.traverse_list()

    data = [2, 40, 90, 100]
    linked_list2 = LinkedList()
    linked_list2.create_list(data)
    linked_list2.traverse_list()
    merge_sorted_ll(linked_list1.head, linked_list2.head)
