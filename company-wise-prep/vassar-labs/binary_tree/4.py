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


def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

# print(height(root))

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
    return ans[0]
print(diameter(root))