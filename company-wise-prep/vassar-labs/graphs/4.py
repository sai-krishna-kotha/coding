from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # For undirected graph, add both ways
    def add_edge_undirected(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # For directed graph, add one way
    def add_edge_directed(self, u, v):
        self.graph[u].append(v)

    def print_graph(self):
        for node, nbrs in self.graph.items():
            print(node, "->", nbrs)

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=" ")

    for nbr in graph[node]:
        if nbr not in visited:
            dfs(graph, nbr, visited)

def bfs(graph, start):
    visited = set()
    q = deque([start])
    visited.add(start)

    while q:
        node = q.popleft()
        print(node, end=" ")

        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                q.append(nbr)

g = Graph()

g.add_edge_undirected(1, 2)
g.add_edge_undirected(1, 3)
g.add_edge_undirected(2, 4)
g.add_edge_undirected(2, 6)
g.add_edge_undirected(3, 5)
g.add_edge_undirected(3, 6)

print("Graph:")
g.print_graph()

print("\nDFS:")
dfs(g.graph, 1)

print("\nBFS:")
bfs(g.graph, 1)
