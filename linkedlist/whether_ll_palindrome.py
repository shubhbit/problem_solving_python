"""
linked-list palindrome can be checked using below 3 methods:
1. using stack
2. reversing linked list
3. using recursion

here in this solution, I will only solve it using stack- simplest
"""

from linkedlist import LinkedList


def is_ll_palindrome(head):
    stack = []
    is_palindrome = True
    copy = head
    while copy:
        stack.append(copy.value)
        copy = copy.next

    while head:
        if head.value != stack.pop():
            is_palindrome = False
            break
        head = head.next
    return is_palindrome
    
    

if __name__ == "__main__":
    data1 = [1, 34, 23, 98, 1, 29, 3]
    linked_list1 = LinkedList()
    linked_list1.create_list(data1)
    linked_list1.traverse_list()
    print("linked-list is palindrome..") if is_ll_palindrome(linked_list1.head) else print("linked-list is not palindrome..")
    data2 = [1, 34, 23, 98, 23, 34, 1]
    linked_list2 = LinkedList()
    linked_list2.create_list(data2)
    linked_list2.traverse_list()
    print("linked-list is palindrome..") if is_ll_palindrome(linked_list2.head) else print("linked-list is not palindrome..")
