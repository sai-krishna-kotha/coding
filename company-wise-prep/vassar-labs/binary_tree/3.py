from collections import defaultdict, deque
class TreeNode:
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.left = None
        self.right = None
    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        print(root.data, end=' ')
        self.in_order(root.right)
    def pre_order(self, root):
        if not root:
            return 
        print(root.data, end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)
    def post_order(self, root):
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.data, end=" ")
    

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(25)


def vertical_order(root):
    if not root:
        return []
    q = deque([(root, 0)])
    mp = defaultdict(list)
    while q:
        node, temp = q.popleft()
        mp[temp].append(node.data)
        if node.left:
            q.append((node.left, temp - 1))
        if node.right:
            q.append((node.right, temp + 1))
    for temp in sorted(mp):
        print(mp[temp], end=' ')
vertical_order(root)