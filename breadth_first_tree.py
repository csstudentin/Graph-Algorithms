from collections import deque

def bfs(adj, s):
    # adj: adjacency list
    # s: start node
    n = len(adj)
    if n == 0:
        return [], []
    visited = [False] * n
    parent = [-1] * n # -1 no parent
    visited[s] = True
    queue = deque([s])

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)
    
    return visited, parent


def build_breadth_first_tree(adj, start):
    n = len(adj)
    if n == 0:
        return []
    _, parent = bfs(adj, start)
    tree_adj = [[] for _ in range(n)]

    for v in range(n):
        u = parent[v]
        if u != -1:
            tree_adj[u].append(v)

    return tree_adj
