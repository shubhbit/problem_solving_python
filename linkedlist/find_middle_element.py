from linkedlist import LinkedList


def find_middle_element(head):
    count = 0
    slow = head
    fast = head
    while fast.next != None:
        count += 1
        slow = slow.next
        if fast.next.next != None:
            fast = fast.next.next
        else:
            break
        

    print("middle element: ", slow.value)


if __name__ == "__main__":
    data = [1, 34, 23, 98, 1, 29, 3]
    linked_list = LinkedList()
    linked_list.create_list(data)
    find_middle_element(linked_list.head)
    data = [34, 78, 90, 23, 43, 93, 87, 65, 11, 65]
    linked_list = LinkedList()
    linked_list.create_list(data)
    find_middle_element(linked_list.head)
    data = [12,90,32,45,6,34,89,5,7,3,54,66,57,200,344,455]
    linked_list = LinkedList()
    linked_list.create_list(data)
    find_middle_element(linked_list.head)
    data = [12,90,32,45,6,34,89,5,7,3,54,66,57,200,344,455,90]
    linked_list = LinkedList()
    linked_list.create_list(data)
    find_middle_element(linked_list.head)

# head     node1    node2     node3     node4     node5      node6
#   1      34,2     78,3      90,4      23,5      43,6       54, None



# head     node1    node2     node3     node4     node5     node6    node7
#   1      34,2     78,3      90,4      23,5      43,6      93,7     87,None
