class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None  
    
def delNode(root, x):
    if root is None:
        return root
    if root.data > x:
        root.left = delNode(root.left, x)
    elif root.data < x:
        root.right = delNode(root.right, x)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        succ = getSuccessor(root)
        root.data = succ.data
        root.right = delNode(root.right, succ.data)
    return root
    
def getSuccessor(root):
    root = root.right
    while root and root.left:
        root = root.left
    return root

def insert(root, data):
    temp = root
    while True:
        if temp.data > data:
            if temp.left != None:
                temp = temp.left
            else:
                temp.left = Node(data)
                break
        else:
            if temp.right != None:
                temp = temp.right
            else:
                temp.right = Node(data)
                break
            
def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print(root.data)
    inorder(root.right)


bst = Node(5)
insert(bst, 3)
insert(bst, 9)
insert(bst, 1)
insert(bst, 4)
insert(bst, 7)
insert(bst, 11)

inorder(bst)
delNode(bst, 5)
inorder(bst)