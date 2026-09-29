from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
    def add_edge_undirected(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
g = Graph()
g.add_edge_undirected(1,2)
g.add_edge_undirected(2,5)
g.add_edge_undirected(2,6)
g.add_edge_undirected(1,3)
g.add_edge_undirected(4,3)
g.add_edge_undirected(7,3)
g.add_edge_undirected(7,8)
g.add_edge_undirected(4,8)

s = Graph()
s.add_edge_undirected(0,1)
s.add_edge_undirected(2,1)
s.add_edge_undirected(2,3)
s.add_edge_undirected(4,5)

def bfs(g, s, V):
    ans = []
    queue = deque([s])
    vis = [0] * (V+1)
    vis[s] = True
    while queue:
        node = queue.popleft()
        ans.append(node)
        for nbr in g.adj[node]:
            if not vis[nbr]:
                vis[nbr] = 1
                queue.append(nbr)
    return ans

# ans = bfs(g, 1, 8)
# print(f"BFS is {ans}")

def dfs(g, s, vis, ans):
    vis[s] = 1
    ans.append(s)
    for nbr in g.adj[s]:
        if not vis[nbr]:
            dfs(g, nbr, vis, ans)
def main_dfs(g):
    V = 8
    vis = [0]*(V+1)
    ans = []
    dfs(g, 1, vis, ans)
    print(f"DFS is {ans}")
# main_dfs(g)

def connected_components(g, s, V):
    vis = [False] * (V+1)
    ans = 0
    for i in range(V+1):
        if not vis[i]:
            ans += 1
            vis[i] = True
            q = deque([i])
            while q:
                node = q.popleft()
                for nbr in g.adj[node]:
                    if not vis[nbr]:
                        vis[nbr] = True
                        q.append(nbr)
    return ans

ans = connected_components(s, 0, 6)
print(f"Connected components are {ans}")

def connected_componenets_dfs(g, V):
    def dfs(g, s, vis):
        vis[s] = 1
        for nbr in g.adj[s]:
            if not vis[nbr]:
                dfs(g, nbr, vis)
    vis = [0]*(V+1)
    ans = 0
    for i in range(0, V+1):
        if not vis[i]:
            dfs(g, i, vis)
            ans += 1
    return ans
ans = connected_componenets_dfs(s, 6)
print(f"Connected components are {ans}")