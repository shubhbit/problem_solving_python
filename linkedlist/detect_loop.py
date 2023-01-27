from node import Node

# k = 3
# 1->2->3->4->5->6
# 4->5->6->1->2->3

class CustomNode(Node):
    def __init__(self, val):
        super().__init__(val)
        self.traversed = False

def detect_loop_hashmap(head):
    hash_map = set()
    while head:
        if head in hash_map:
            print("there is loop in linked list")
            return
        hash_map.add(head)
        head = head.next
    print("There is no loop in linked list")

def detect_loop_traversed(head):
    while head:
        if head.traversed:
            print("there is loop in linked list")
            return
        head.traversed = True
        head = head.next
    print("there is no loop in linked list")

def detect_loop_flyod_cycle(head):
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print("there is loop in linked list")
            return

    print("there is no loop in linked list")



if __name__ == "__main__":

    # 1 -> 2 -> 3 -> 4 -> 5
    #           <|________|
    
    

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head.next.next
    detect_loop_hashmap(head)
    #########################################
    del head
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    detect_loop_hashmap(head)
    #########################################

    head = CustomNode(1)
    head.next = CustomNode(2)
    head.next.next = CustomNode(3)
    head.next.next.next = CustomNode(4)
    head.next.next.next.next = CustomNode(5)
    head.next.next.next.next.next = head.next.next
    detect_loop_traversed(head)
    #########################################
    del head
    head = CustomNode(1)
    head.next = CustomNode(2)
    head.next.next = CustomNode(3)
    head.next.next.next = CustomNode(4)
    head.next.next.next.next = CustomNode(5)
    detect_loop_traversed(head)
    #########################################

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head.next.next
    detect_loop_flyod_cycle(head)
    #########################################
    del head
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    detect_loop_flyod_cycle(head)
    #########################################