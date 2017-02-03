from Queue import *

class Node:

    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def bfs_print(head):

    thisLevel = Queue()
    thisLevel.put(head)

    while not thisLevel.empty():
        for elemInLevel in range(thisLevel.qsize()):
            elementGot = thisLevel.get()
            print elementGot.data,
            if elementGot.left:
                thisLevel.put(elementGot.left)
            if elementGot.right:
                thisLevel.put(elementGot.right)
        print
        
def bfs(root):
    
    bList = []
    bList.append(root)
    while len(bList) > 0:
        print bList[0].data,
        node = bList.pop(0)
        if node.left:
            bList.append(node.left)
        if node.right:
            bList.append(node.right)
            

t = Node(1, Node(2, Node(4, Node(7))), Node(3, Node(5), Node(6)))
#bfs_print(t)
