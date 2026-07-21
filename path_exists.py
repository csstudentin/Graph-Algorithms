from collections import deque


def path_exists(adj, source, dest):
    """
    Check if a path exists from source to dest using BFS
    """
    # adj: adjacency list
    n = len(adj)
    if n == 0 or source < 0 or source >= n or dest < 0 or dest >= n:
        return False
    if source == dest:
        return True
    # operate bfs
    visited = [False] * n
    visited[source] = True
    queue = deque([source])

    while queue:
        u = queue.popleft() # dequeue
        for v in adj[u]:
            if v == dest:
                return True
            if not visited[v]:
                visited[v] = True
                queue.append(v) # enqueue
    
    return False
