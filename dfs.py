class Node:

    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def preOrder(root):
    if root is None:
        return
    print root.data
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)

def inOrder(root):
    if root is None:
        return
    if root.left:
        preOrder(root.left)
    print root.data
    if root.right:
        preOrder(root.right)

def postOrder(root):
    if root is None:
        return
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)
    print root.data

t = Node(1, Node(2, Node(4, Node(7))), Node(3, Node(5), Node(6)))
preOrder(t)
print
inOrder(t)
print
postOrder(t)
