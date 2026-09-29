class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
t1 = Node(1)
t1.left = Node(2)
t1.right = Node(5)
t1.left.left = Node(3)
t1.left.right = Node(4)
t1.right.left = Node(6)
t1.right.right = Node(7)
# t1.right.right.left = Node(8)

# dfs 
# 1. pre-order traversal
# N L R
def pre_order(root, ans):
    if not root:
        return None
    # print(root.val)
    ans.append(root.val)
    pre_order(root.left, ans)
    pre_order(root.right, ans)
# ans = []
# pre_order(t1, ans)
# print(f"Pre-order traversal is {ans}")


# 2. in-order traversal
# L N R
def in_order(root, ans):
    if not root:
        return None
    # print(root.val)
    in_order(root.left, ans)
    ans.append(root.val)
    in_order(root.right, ans)
# ans = []
# in_order(t1, ans)
# print(f"In-order traversal is {ans}")

# 3. post-order traversal
# L R N
def post_order(root, ans):
    if not root:
        return None
    # print(root.val)
    post_order(root.left, ans)
    post_order(root.right, ans)
    ans.append(root.val)
# ans = []
# post_order(t1, ans)
# print(f"Post-order traversal is {ans}")


def iterative_preorder(root):
    stack = [root]
    ans = []
    while stack:
        node = stack.pop()
        ans.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return ans
# ans = iterative_preorder(t1)
# print(f"Iterative PreOder traversal is {ans}")

def iterative_inorder(root):
    stack = []
    ans = []
    node = root
    while True:
        if node:
            stack.append(node)
            node = node.left
        else:
            if len(stack) == 0:
                break
            node = stack.pop()
            ans.append(node.val)
            node = node.right
    return ans
# ans = iterative_inorder(t1)
# print(f"Iterative InOrder traversal is {ans}")

def iterative_postorder(root):
    stack1 = [root]
    stack2 = []
    ans = []
    while stack1:
        node = stack1.pop()
        stack2.append(node.val)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        ans.append(stack2.pop())
    return ans
# ans = iterative_postorder(t1)
# print(f"Iterative PostOrder traversal is {ans}")

from collections import deque
def level_order_traversal(root):
    queue = deque([root])
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
        ans.append(temp)
    return ans
# ans = level_order_traversal(t1)
# print(f"Level order traversal is {ans}")

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))
# ans = height(t1)
# print(f"Height of tree is {ans}")

def diameter(root, ans):
    if not root:
        return 0
    lh = diameter(root.left, ans)
    rh = diameter(root.right, ans)
    ans[0] = max(ans[0], lh+rh)
    return 1 + max(lh, rh)
# ans = [0]
# diameter(t1, ans)
# print(f"Diameter of a tree is {ans[0]}")

def maxPathSum(root, ans):
    if not root:
        return 0
    lh = maxPathSum(root.left, ans)
    rh = maxPathSum(root.right, ans)
    ans[0] = max(ans[0], root.val + lh + rh)
    return root.val + max(lh,rh)
# ans = [0]
# maxPathSum(t1, ans)
# print(f"MaxPathSum of tree is {ans[0]}")

def boundary_traversal(root):
    if not root: return []
    def get_left_nodes(root):
        temp = root
        ans = []
        while temp:
            if temp.left or temp.right:
                ans.append(temp.val)
            if temp.left:
                temp = temp.left
            else:
                temp = temp.right
        return ans
    def get_leaf_nodes(root, ans):
        if not root:
            return
        if not root.left and not root.right:
            ans.append(root.val)
            return 
        get_leaf_nodes(root.left, ans)
        get_leaf_nodes(root.right, ans)
    def get_right_nodes(root):
        ans = []
        # root = root.right
        while root:
            if root.left or root.right:
                ans.append(root.val)
            if root.right:
                root = root.right
            else:
                root = root.left
        return ans[::-1]
        
    left_nodes = get_left_nodes(root)
    leaf_nodes = []
    get_leaf_nodes(root.left, leaf_nodes)
    right_nodes = get_right_nodes(root.right)
    # print(f"Left nodes {left_nodes}")
    # print(f"Leaf nodes {leaf_nodes}")
    # print(f"Right nodes {right_nodes}")
    
    return [root.val] +  left_nodes + leaf_nodes + right_nodes

t2 = Node(1)
t2.left = Node(2)
t2.left.left = Node(3)
t2.left.left.right = Node(4)
t2.left.left.right.left = Node(5)
t2.left.left.right.right = Node(6)
t2.right = Node(7)
t2.right.right = Node(8)
t2.right.right.left = Node(9)
t2.right.right.left.left = Node(10)
t2.right.right.left.right = Node(11)

# ans = boundary_traversal(t2)
# print(f"Boundary traversal is {ans}")

from collections import defaultdict
from heapq import heappop, heappush
def vertical_order_traversal(root):
    queue = deque([(root, 0, 0)])
    heap = []
    while queue:
        node, hd, level = queue.popleft()
        heappush(heap, (hd, level, node.val))
        if node.left:
            queue.append((node.left, hd - 1, level + 1))
        if node.right:
            queue.append((node.right, hd + 1, level + 1))
    prev_hd = None
    ans = []
    while heap:
        hd, level, val = heappop(heap)
        if prev_hd != hd:
            ans.append([])
            prev_hd = hd
        ans[-1].append(val)
    return ans

# ans = vertical_order_traversal(t2)
# print(f"Vertical Order traversal is {ans}")

def right_view(root, level,  ans):
    if not root:
        return 
    if len(ans) == level:
        ans.append(root.val)
    right_view(root.right, level+1, ans)
    right_view(root.left, level + 1, ans)
# ans = []
# right_view(t1, 0, ans)
# print(f"Right view is {ans}")

def left_view(root, level, ans):
    if not root:
        return
    if len(ans) == level:
        ans.append(root.val)
    left_view(root.left, level+1, ans)
    left_view(root.right, level+1, ans)
# ans = []
# left_view(t1, 0, ans)
# print(f"Left view is {ans}")

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
def symmetric_tree(root1, root2):
    if not root1 or not root2:
        return root1 == root2
    return root1.val == root2.val and symmetric_tree(root1.left, root2.right) and symmetric_tree(root1.right, root2.left)

# print(f"Is symmetic? {symmetric_tree(root.left, root.right)}")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

def getPath(root, arr, x):
    if not root:
        return False
    arr.append(root.val)
    if root.val == x:
        return True
    if getPath(root.left, arr, x) or getPath(root.right, arr, x):
        return True
    arr.pop()
    return False
# arr = []
# getPath(root, arr, 7)
# print(f"Root to leaf path :{arr}")

def LCA(root, p, q):
    arr1 = []
    getPath(root, arr1, p)
    arr2 = []
    getPath(root, arr2, q)
    low = 0
    high = min(len(arr1), len(arr2)) - 1
    while low <= high:
        mid = (low+high)//2
        if arr1[mid] == arr2[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return arr1[high]
# print(f"LCA of p and q is {LCA(root, 4, 7)}")

def LCA_opt(root, p, q):
    if not root or root.val == p or root.val == q:
        return root
    left = LCA_opt(root.left, p, q)
    right = LCA_opt(root.right, p, q)
    if not left:
        return right
    elif not right:
        return left
    else:
        return root
# print(f"LCA of p and q is {LCA(root, 5, 7)}")

def max_width(root):
    queue = deque([(root, 0)])
    ans = 0
    while queue:
        first = queue[0][1]
        last = queue[-1][1]
        ans = max(ans, last - first + 1)
        for _ in range(len(queue)):
            node, curr_idx = queue.popleft()
            if node.left:
                queue.append((node.left, 2 * curr_idx))
            if node.right:
                queue.append((node.right, 2 * curr_idx + 1))
    return ans
print(f"Max width of tree is {max_width(root)}")