class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

def traversals(root):
    pre_order = []
    in_order = []
    post_order = []
    queue = [[root, 1]]
    while queue:
        node, num = queue[-1]
        if num == 1:
            pre_order.append(node.val)
            queue[-1][1] += 1
            if node.left:
                queue.append([node.left, 1])
        elif num == 2:
            in_order.append(node.val)
            queue[-1][1] += 1
            if node.right:
                queue.append([node.right, 1])
        else:
            post_order.append(node.val)
            queue.pop()
    return pre_order, in_order, post_order

# a, b, c = traversals(root)
# print(f"pre: {a}\nin: {b}\npost: {c}")

def pre_order(node):
    stack = [node]
    ans = []
    while stack:
        node = stack.pop()
        ans.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return ans

# print(f"pre-order is {pre_order(root)}")

def in_order(node):
    stack = []
    ans = []
    node = root
    while True:
        if node != None:
            stack.append(node)
            node = node.left
        else:
            if len(stack) == 0:
                break
            node = stack.pop()
            ans.append(node.val)
            node = node.right
    return ans

# print(f"InOrder Traversal is {in_order(root)}")

def post_order(node):
    stk1 = [root]
    stk2 = []
    ans = []
    while stk1:
        node = stk1.pop()
        stk2.append(node)
        if node.left:
            stk1.append(node.left)
        if node.right:
            stk1.append(node.right)
    while stk2:
        ans.append(stk2.pop().val)
    return ans

# print(f"Post Order Traversal is {post_order(root)}")

def diameter(root, ans):
    if not root:
        return 0
    lh = diameter(root.left, ans)
    rh = diameter(root.right, ans)
    ans[0] = max(ans[0], lh+rh)
    return 1 + max(lh, rh)
# ans = [0]
# diameter(root, ans)
# print(f"Diameter is {ans[0]}")

def max_path_sum(root, ans):
    if not root:
        return 0
    lh = max_path_sum(root.left, ans)
    rh = max_path_sum(root.right, ans)
    ans[0] = max(ans[0], lh+root.val+rh)
    return root.val + max(lh, rh)
# ans = [0]
# max_path_sum(root, ans)
# print(f"MaxPath Sum is {ans[0]}")

def identical_trees(p, q):
    if p == None and q == None:
        return True
    if p == None or q == None:
        return False
    return p.val == q.val and identical_trees(p.left, q.left) and identical_trees(p.right, q.right)

from collections import deque
def zigzag(root):
    queue = deque([root])
    flag = 0
    ans = []
    while queue:
        temp = []
        for _ in range(len(queue)):
            node = queue.popleft()
            temp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if flag == 0:
            ans.append(temp)
            flag = 1
        else:
            temp.reverse()
            ans.append(temp)
            flag = 0
    return ans
# ans = zigzag(root)
# print(f"Zigzag traversal is {ans}")

from collections import defaultdict
def vertical_order(root):
    queue = deque([(root, 0)])
    mapp = defaultdict(list)
    ans = []
    while queue:
        node, hd = queue.popleft()
        mapp[hd].append(node.val)
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    for hd in sorted(mapp):
        ans.append(mapp[hd])
    return ans

# ans = vertical_order(root)
# print(f"Vertical Order is {ans}")

def left_view(root):
    queue = deque([root])
    ans = []
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if i == 0:
                ans.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return ans
# ans = left_view(root)
# print(f"Left view is {ans}")

def right_view(root):
    queue = deque([root])
    ans = []
    while queue:
        n = len(queue)
        for i in range(n):
            node = queue.popleft()
            if i == n - 1:
                ans.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return ans
ans = right_view(root)
print(f"Right view is {ans}")

def top_view(root):
    queue = deque([(root, 0)])
    mapp = {}
    ans = []
    while queue:
        node, hd = queue.popleft()
        if hd not in mapp:
           mapp[hd] = node.val
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    for hd in sorted(mapp):
        ans.append(mapp[hd])
    return ans
# ans = top_view(root)
# print(f"Top View is {ans}")

def bottom_view(root):
    queue = deque([(root, 0)])
    mapp = defaultdict(int)
    while queue:
        node, hd = queue.popleft()
        mapp[hd] = node.val
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    ans = []
    for hd in sorted(mapp):
        ans.append(mapp[hd])
    return ans
ans = bottom_view(root)
print(f"Bottom View is {ans}")
