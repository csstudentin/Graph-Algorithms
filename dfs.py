INF = float('inf')

def dfs_recursive(adj, start):
    # adj: adjacency list
    n = len(adj)
    if n == 0 or start < 0 or start >= n:
        return None
    visited = [False] * n
    distance = [INF] * n 
    parent = [-1] * n # -1 no parent
    start_time = [-1] * n # start time of process
    finish_time = [-1] * n # finish time of process
    # initial
    visited[start] = True
    distance[start] = 0
    time = 0

    def dfs_visit(v):
        nonlocal time
        time += 1
        visited[v] = True
        start_time[v] = time
        for u in adj[v]:
            if not visited[u]:
                distance[u] = distance[v] + 1
                parent[u] = v
                dfs_visit(u)
        time += 1
        finish_time[v] = time

    dfs_visit(start)

    return visited, distance, parent, start_time, finish_time


def dfs_three_state_color_recursive(adj, start):
    # adj: adjacency list
    n = len(adj)
    if n == 0 or start < 0 or start >= n:
        return None
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    distance = [INF] * n 
    parent = [-1] * n # -1 no parent
    start_time = [-1] * n # start time of process
    finish_time = [-1] * n # finish time of process
    # initial
    distance[start] = 0
    time = 0

    def dfs_visit(v):
        nonlocal time
        color[v] = GRAY
        time += 1
        start_time[v] = time
        for u in adj[v]:
            if color[u] == WHITE:
                distance[u] = distance[v] + 1
                parent[u] = v
                dfs_visit(u)
        color[v] = BLACK
        time += 1
        finish_time[v] = time

    dfs_visit(start)

    return color, distance, parent, start_time, finish_time


def dfs(adj, start):
    # adj: adjacency list
    n = len(adj)
    if n == 0 or start < 0 or start >= n:
        return None
    visited = [False] * n
    distance = [INF] * n 
    parent = [-1] * n # -1 no parent
    start_time = [-1] * n # start time of process
    finish_time = [-1] * n # finish time of process
    # initial
    visited[start] = True
    distance[start] = 0
    stack = [start]
    time = 0

    while stack:
        v = stack.pop()
        time += 1
        start_time[v] = time
        for u in adj[v]:
            if not visited[u]:
                visited[u] = True
                distance[u] = distance[v] + 1
                parent[u] = v
                stack.append(u) # push node
    
    return visited, distance, parent


def dfs_advanced(adj, start):
    """Iterative DFS returning color, distance, parent, start_time, finish_time"""
    n = len(adj)
    if n == 0 or start < 0 or start >= n:
        return None
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    distance = [INF] * n
    parent = [-1] * n
    start_time = [-1] * n
    finish_time = [-1] * n
    # initial
    distance[start] = 0
    stack = [start]
    time = 0

    while stack:
        v = stack.pop()
        if color[v] == WHITE:
            # First discovery
            color[v] = GRAY
            time += 1
            start_time[v] = time
            # Push back to finish later
            stack.append(v)
            for u in adj[v]:
                if color[u] == WHITE:
                    distance[u] = distance[v] + 1
                    parent[u] = v
                    stack.append(u)
        elif color[v] == GRAY:
            # All children processed
            color[v] = BLACK
            time += 1
            finish_time[v] = time

    return color, distance, parent, start_time, finish_time


