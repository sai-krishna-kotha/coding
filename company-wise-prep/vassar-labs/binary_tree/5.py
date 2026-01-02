from collections import deque


def isIdenticalDFS(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.data != q.data:
        return False
    return isIdenticalDFS(p.left, q.left) and isIdenticalDFS(p.right, q.right)

def isIdenticalBFS(p, q):
    queue = deque([(p, q)])
    while queue:
        a, b = queue.popleft()
        if not a and not b:
            continue
        if not a or not b:
            return False
        if a.data != b.data:
            return False
        queue.append((a.left, b.left))
        queue.append((a.right, b.right))
    return True

