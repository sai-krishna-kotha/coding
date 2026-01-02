from collections import deque

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
    def preorder_iterative(self, root):
        if not root:
            return
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            print(node.data, end=" ")
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(25)

def top_view(root):
    queue = deque([(root, 0)])
    mp = {}
    while queue:
        node, hd = queue.popleft()
        if hd not in mp:
            mp[hd] = node.data
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    for hd in sorted(mp):
        print(mp[hd], end = ' ')
# top_view(root)

def bottom_view(root):
    queue = deque([(root, 0)])
    mp = {}
    while queue:
        node, hd = queue.popleft()
        mp[hd] = node.data
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    for hd in sorted(mp):
        print(mp[hd])
# bottom_view(root)

def left_view(root):
    queue = deque([root])
    ans = []
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if i == 0:
                ans.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return ans

# print(left_view(root))

def right_view(root):
    queue = deque([root])
    ans = []
    while queue:
        n = len(queue)
        for i in range(n):
            node = queue.popleft()
            if i == n-1:
                ans.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return ans

print(right_view(root))