#                                [50]
#                             /        \
#                         [20]          [45]
#                        /    \        /    \
#                    [11]      [15]  [30]    [78]


from tree import implement_tree

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end="->")
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.data,  end="->")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end="->")

if __name__ == "__main__":
    root = implement_tree()
    print("inorder traversal:")
    inorder_traversal(root)
    print("\npreorder traversal:")
    preorder_traversal(root)
    print("\npostorder traversal:")
    postorder_traversal(root)

