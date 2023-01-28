from node import Node


def detect_loop(head):
    hashmap = set()
    while head.next is not None:
        if head.next in hashmap:
            return head
        hashmap.add(head)
        head = head.next


def remove_loop(head):
    is_loop = detect_loop(head)
    if is_loop:
        is_loop.next = None
        print("loop removed, please check..")
    else:
        print("there is no loop, no removal required")


if __name__ == "__main__":

    # 1 -> 2 -> 3 -> 4 -> 5
    #           <|________|

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head.next.next
    remove_loop(head)
    print("still there is loop") if detect_loop(head) else print(
        "either there was no loop or loop removed")
    #########################################
    del head
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    remove_loop(head)
    print("still there is loop") if detect_loop(head) else print(
        "either there was no loop or loop removed")
    #########################################
