from collections import deque


def vertex_disjoint_paths_using_bfs(adj, source, dest):
    """
    Find paths which include disjoint verteces
    """
    # adj: adjacency list
    n = len(adj)
    if n == 0 or source < 0 or source >= n or dest < 0 or dest >= n:
        return None
    if source == dest:
        return []
    selected = [False] * n
    all_paths = []
    while True:
        path = find_path_bfs(adj, selected, source, dest)
        if not path:
            break
        all_paths.append(path)
        if len(path) == 2:
            break
        
    return all_paths


def find_path_bfs(adj, selected, source, dest):
    n = len(adj)
    visited = [False] * n
    parent = [-1] * n

    visited[source] = True
    queue = deque([source])

    found = False
    while queue and not found:
        u = queue.popleft()
        for v in adj[u]:
            if v == dest:
                parent[dest] = u
                found = True
                break
            if not selected[v] and not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.append(v)

    if not found:
        return []
    
    # reconstruct path
    v = dest
    path = []
    while v != -1:
        path.append(v)
        if v != source and v != dest:
            selected[v] = True
        v = parent[v]
    path.reverse()
    return path


