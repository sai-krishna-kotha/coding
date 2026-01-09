from collections import deque

def even_odd_level_sum(root):
    if not root:
        return 0, 0
    
    q = deque([root])
    level = 1
    
    odd_sum = 0
    even_sum = 0
    
    while q:
        size = len(q)
        
        for _ in range(size):
            node = q.popleft()
            
            if level % 2 == 1:
                odd_sum += node.data
            else:
                even_sum += node.data
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        level += 1
    
    return odd_sum, even_sum
