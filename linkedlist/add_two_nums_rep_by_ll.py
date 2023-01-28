# Given two decimal numbers represented by two linked lists of size N and M respectively.
# The task is to return a linked list that represents the sum of these two numbers.

# For example, the number 190 will be represented by the linked list, 1->9->0->null,
# similarly 25 by 2->5->null. Sum of these two numbers is 190 + 25 = 215,
# which will be represented by 2->1->5->null.
# You are required to return the head of the linked list 2->1->5->null.


from linkedlist import LinkedList


def sum_two_nums(head1, head2):
    num1 = ""
    num2 = ""
    while head1:
        num1 += str(head1.value)
        head1 = head1.next
    while head2:
        num2 += str(head2.value)
        head2 = head2.next
    resultant_num = int(num1) + int(num2)
    resultant_num = list(str(resultant_num))
    resultant_ll = LinkedList()
    resultant_ll.create_list(resultant_num)
    return resultant_ll


if __name__ == "__main__":
    data = [1, 9, 0]
    linked_list1 = LinkedList()
    linked_list1.create_list(data)
    linked_list1.traverse_list()

    data = {2, 5}
    linked_list2 = LinkedList()
    linked_list2.create_list(data)
    linked_list2.traverse_list()

    resultant_ll = sum_two_nums(linked_list1.head, linked_list2.head)
    resultant_ll.traverse_list()
