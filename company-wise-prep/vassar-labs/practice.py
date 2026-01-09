from collections import deque, defaultdict

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def inorder(self, root):
        if not root:
            return None
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)
        
    def inorder_iterative(self, root):
        stack = []
        ans = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ans.append(curr.data)
            curr = curr.right
        # return ans
        print(ans)
        
    def preorder(self, root):
        if not root:
            return None
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right) 
        
    def preorder_iterative(self, root):
        stack = [root] if root else []
        ans = []
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.data)
                if node.right:
                    ans.append(node.right)
                if node.left:
                    ans.append(node.left)
        print(ans)
        # return ans

    def postorder(self, root):
        if not root:
            return None
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)
    def postorder_iterative(self, root):
        stack1 = [root] if root else []
        stack2 = []
        ans = []
        while stack1:
            node = stack1.pop()
            if node:
                stack2.append(node)
                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)
        while stack2:
            ans.append(stack2.pop().data)
        print(ans)
        return ans
    def level_order_traversal(self, root):
        queue = deque([root])
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(ans)
        return ans
    def vertical_order_traversal(self, root):
        queue = deque([(root, 0)])
        mapp = defaultdict(list)
        while queue:
            node, hd = queue.popleft()
            mapp[hd].append(node.data)
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        ans = []
        for hd in sorted(mapp):
            ans.append(mapp[hd])
        print(ans)
        return ans
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

def diameter(root):
    ans = [0]
    def solve(root):
        if not root:
            return 0
        lh = solve(root.left)
        rh = solve(root.right)
        ans[0] = max(ans[0], lh+rh)
        return 1 + max(lh, rh)
    solve(root)
    # print(ans[0])
    return ans[0]

def isIdentical(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.data != root2.data:
        return False
    return isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)

def top_view(root):
    queue = deque([(root, 0)])
    mapp = {}
    while queue:
        node, hd = queue.popleft()
        if hd not in mapp:
            mapp[hd] = node.data
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    ans = []
    for hd in sorted(mapp):
        ans.append(mapp[hd])
    # print(ans)
    return ans

def bottoom_view(root):
    queue = deque([(root, 0)])
    mapp = {}
    while queue:
        node, hd = queue.popleft()
        mapp[hd] = node.data
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    ans = []
    for hd in sorted(mapp):
        ans.append(mapp[hd])
    # print(ans)
    return ans

def left_view(root):
    queue = deque([root])
    ans = []
    while queue:
        n = len(queue)
        for i in range(n):
            node = queue.popleft()
            if i == 0:
                ans.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    # print(ans)
    return ans

def right_view(root):
    queue = deque([root])
    ans = []
    while queue:
        n = len(queue)
        for i in range(n):
            node = queue.popleft()
            if i == n - 1:
                ans.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    # print(ans)
    return ans

bt = Node(1)
bt.left = Node(2)
bt.right = Node(3)
bt.left.left = Node(4)
bt.left.right = Node(5)
bt.right.left = Node(6)
bt.right.right = Node(7)

bt2 = Node(1)
bt2.left = Node(2)
bt2.right = Node(3)
bt2.left.left = Node(4)
bt2.left.right = Node(5)
bt2.right.left = Node(6)
bt2.right.right = Node(7)

# bt.inorder(bt)
# bt.inorder_iterative(bt)
# bt.preorder(bt)
# bt.preorder(bt)
# bt.postorder(bt)
# bt.postorder_iterative(bt)
# bt.level_order_traversal(bt)
# bt.vertical_order_traversal(bt)
# ans = height(bt)
# print(ans)
# print(diameter(bt))
# print(isIdentical(bt, bt2))
# print(top_view(bt))
# print(bottoom_view(bt))
# print(left_view(bt))
print(right_view(bt))