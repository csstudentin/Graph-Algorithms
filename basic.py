"""
adj is adjacency list graph
"""

def remove_self_loops(adj):
    """Return a new adjacency list without self-loops."""
    n = len(adj)
    if n == 0:
        return []
    new_adj = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            if v != u:
                new_adj[u].append(v)
    return new_adj


def find_min_max_degree(adj):
    n = len(adj)
    if n == 0:
        return 0, 0
    mn = mx = len(adj[0])
    for i in range(1, n):
        mn = min(mn, len(adj[i]))
        mx = max(mx, len(adj[i]))
    return mn, mx


def complement_graph(adj):
    n = len(adj)
    if n == 0:
        return []
    complement_adj = [[] for _ in range(n)]
    for v in range(n):
        visited = [False] * n
        for u in adj[v]:
            visited[u] = True
        visited[v] = True # no self loop 
        for i in range(n):
            if not visited[i]:
                complement_adj[v].append(i)
    return complement_adj


def reverse_graph(adj):
    n = len(adj)
    if n == 0:
        return []
    rev_adj = [[] for _ in range(n)] # reverse adjacenty list
    for v in range(n):
        for u in adj[v]:
            if v not in rev_adj[u]:
                rev_adj[u].append(v)
    return rev_adj


def convert_adj_list_to_edge_list(adj):
    n = len(adj)
    if n == 0:
        return []
    edges = []
    for v in range(n):
        for u in adj[v]:
            edges.append((v, u))
    return edges


def convert_edge_list_to_adj_list(edges, directed=True):
    if not edges:
        return []
    # Find the maximum vertex index
    max_node = max(max(u, v) for u, v in edges)
    n = max_node + 1
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    return adj


def is_directed_graph(adj):
    n = len(adj)
    if n == 0:
        return False
    for u in range(n):
        for v in adj[u]:
            if u not in adj[v]:
                return True
    return False


def find_max_min_weight(adj):
    n = len(adj)
    if n == 0:
        return None

    max_edge = None
    min_edge = None
    max_w = -float('inf')
    min_w = float('inf')

    for u in range(n):
        for v, w in adj[u]:
            # Update max
            if w > max_w:
                max_w = w
                max_edge = (u, v, w)
            # Update min
            if w < min_w:
                min_w = w
                min_edge = (u, v, w)

    return max_edge, min_edge
