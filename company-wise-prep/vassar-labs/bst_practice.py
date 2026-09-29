class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
def insert(root, data):
    if not root:
        return Node(data)
    temp = root
    while True:
        if data < temp.val:
            if temp.left:
                temp = temp.left
            else:
                temp.left = Node(data)
                break
        elif data > temp.val:
            if temp.right:
                temp = temp.right
            else:
                temp.right = Node(data)
                break
        else:
            break
    return root

t1 = Node(5)
insert(t1, 4)
insert(t1, 7)
insert(t1, 2)
insert(t1, 3)
insert(t1, 6)
insert(t1, 7)

t1 = Node(4)
insert(t1, 3)
insert(t1, 6)
insert(t1, 1)
insert(t1, 2)
insert(t1, 5)
insert(t1, 7)
def inorder_traversal(root):
    stack = []
    ans = []
    temp = root
    while True:
        if temp:
            stack.append(temp)
            temp = temp.left
        else:
            if len(stack) == 0:
                break
            temp = stack.pop()
            ans.append(temp.val)
            temp = temp.right
    return ans

ans = inorder_traversal(t1)
print(f"InOrder Traversal is {ans}")

def delete(root, key):
    if not root:
        return 
    if root.val > key:
        root.left = delete(root.left, key)
    elif root.val < key:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        succ = root.right
        while succ.left:
            succ = succ.left
        root.val = succ.val
        root.right = delete(root.right, succ.val)
    return root

delete(t1, 7)
ans = inorder_traversal(t1)
print(f"InOrder Traversal is {ans}")
# delete(t1, 4)
# ans = inorder_traversal(t1)
# print(f"InOrder Traversal is {ans}")