def isBST(root, left = float("-inf"), right = float("inf")):
    if not root:
        return True
    if not (left < root.data < right):
        return False
    return isBST(root.left, left, root.data) and isBST(root.right, root.data, right)