#                                [50]
#                             /        \
#                         [20]          [45]
#                        /    \        /    \
#                    [11]      [15]  [30]    [78]


class BinaryTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def implement_tree():
    root = BinaryTreeNode(50)
    left_child = BinaryTreeNode(20)
    right_child = BinaryTreeNode(45)
    l2_left_left = BinaryTreeNode(11)
    l2_left_right = BinaryTreeNode(15)
    l2_right_left = BinaryTreeNode(30)
    l2_right_right = BinaryTreeNode(78)
    root.left = left_child
    root.right = right_child
    left_child.left = l2_left_left
    left_child.right = l2_left_right
    right_child.left = l2_right_left
    right_child.right = l2_right_right
    return root

if __name__ == "__main__":
    implement_tree()