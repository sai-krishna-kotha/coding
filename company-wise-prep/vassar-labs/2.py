class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert_to_bst(root, data):
    temp = root
    while True:
        if temp.data <= data:
            if temp.right != None:
                temp = temp.right
            else:
                temp.right = Node(data)
                break
        else:
            if temp.left != None:
                temp = temp.left
            else:
                temp.left = Node(data)
                break
    return root

def insert(root, key):
    if not root:
        return Node(key)
    
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    return root

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def search(root, key):
    if not root:
        return False
    if root.data == key:
        return True
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)

def search_iter(root, key):
    while root:
        if root.data == key:
            return True
        elif key < root.data:
            root = root.left
        else:
            root = root.right
    return False

def floorBST(root, key):
    floor = None
    while root:
        if root.data == key:
            return root.data
        if root.data > key:
            root = root.left
        else:
            floor = root.data
            root = root.right
    return floor

def ceilBST(root, key):
    ceil = None
    while root:
        if root.data == key:
            return root.data
        if root.data < key:
            root = root.right
        else:
            ceil = root.data
            root = root.left
    return ceil

def findMin(root):
    if not root:
        return None
    while root.left:
        root = root.left
    return root.data

def findMax(root):
    if not root:
        return None
    while root.right:
        root = root.right
    return root.data

def LCA(root, p, q):
    while root:
        if p < root.data and q < root.data:
            root = root.left
        elif p > root.data and q > root.data:
            root = root.right
        else:
            return root.data
