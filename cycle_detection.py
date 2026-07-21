from collections import deque

# Detect self loop
def has_self_loop(adj):
    # adj: adjacency list
    n = len(adj)
    if n == 0:
        return False
    for u in range(n):
        for v in adj[u]:
            if u == v:
                return True
    return False


def has_cycle(adj):
    'Detect cycle in undirected graph using DFS (iterative)'
    """
    Uncomment this if you want to check adj is an undirected graph
    from basic import is_directed_graph
    if is_directed_graph(adj):
        return False
    """
    n = len(adj)
    if n == 0:
        return False
    visited = [False] * n

    for start in range(n):
        if not visited[start]:
            visited[start] = True
            stack = [(start, -1)]   # (node, parent)

            while stack:
                v, parent = stack.pop()
                for u in adj[v]:
                    if not visited[u]:
                        visited[u] = True
                        stack.append((u, v))
                    elif u != parent:
                        return True
    return False


def has_cycle_directed_graph(adj):
    'Detect cycle in directed graph using DFS with three state color (iterative)'
    """
    Uncomment this if you want to check adj is a directed graph
    from basic import is_directed_graph
    if not is_directed_graph(adj):
        return False
    """
    n = len(adj)
    if n == 0:
        return False
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n

    for start in range(n):
        if color[start] == WHITE:
            stack = [(start, False)]  # (node, is_finish)

            while stack:
                v, is_finish = stack.pop()
                if not is_finish and color[v] == WHITE:
                    # First discovery
                    color[v] = GRAY
                    # Push sentinel to turn BLACK later
                    stack.append((v, True))
                    for u in adj[v]:
                        if color[u] == GRAY:
                            return True
                        if color[u] == WHITE:
                            stack.append((u, False))
                elif is_finish:
                    color[v] = BLACK

    return False
