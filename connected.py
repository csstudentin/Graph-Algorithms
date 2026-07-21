from collections import deque

def is_connected(adj):
    """check if a graph is connected in direct or undirect graph using BFS"""
    # adj: adjacency list
    n = len(adj)
    if n == 0:
        return False
    visited = [False] * n

    # bfs
    queue = deque([0])
    visited[0] = True

    while queue:
        u = queue.popleft() # dequeue
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

    return all(visited) # all of nodes are visited


def count_connected_components(adj):
    """count connected components in direct or undirect graph using BFS"""
    # adj: adjacency list
    n = len(adj)
    if n == 0:
        return 0
    visited = [False] * n

    def bfs(s):
        queue = deque([s])
        visited[s] = True

        while queue:
            u = queue.popleft() # dequeue
            for v in adj[u]:
                if not visited[v]:
                    visited[u] = True
                    queue.append(v)

    count = 0
    for v in range(n):
        if not visited[v]:
            count += 1
            bfs(v)

    return count

