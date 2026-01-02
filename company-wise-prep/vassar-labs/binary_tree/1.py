class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def add_child(self, parent, child):
        parent.children.append(child)
    def traverse(self, root):
        if root is None:
            return 
        print(root.data, end=" ")
        for child in root.children:
            self.traverse(child)
    
root = TreeNode('A')
b = TreeNode('B')
c = TreeNode('C')
d = TreeNode('D')
e = TreeNode('E')
f = TreeNode('F')

root.add_child(root, b)
root.add_child(b, c)
# print(root.children[0].data)
print(root.traverse(root))