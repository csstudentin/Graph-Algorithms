"""
Breadth First Search Algorithm
adj is adjacenty list
"""
from collections import deque
INF = float('inf')


def bfs(adj, start):
    n = len(adj)
    if n == 0 or start < 0 or start >= n:
        return None
    visited = [False] * n # visited nodes
    distance = [INF] * n # distance of node from start
    parent = [-1] * n # -1 no parent
    # initial
    visited[start] = True
    distance[start] = 0
    queue = deque([start])

    while queue:
        v = queue.popleft() # dequeue vertex

        for u in adj[v]:
            if not visited[u]:
                visited[u] = True
                distance[u] = distance[v] + 1
                parent[u] = v
                queue.append(u)
    return visited, distance, parent


# bfs with three state colors
def bfs_three_color(adj, start):
    n = len(adj)
    if n == 0 or start < 0 or start >= n:
        return None
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    distance = [INF] * n
    parent = [-1] * n
    # Initial
    color[start] = GRAY
    distance[start] = 0
    queue = deque([start])

    while queue:
        v = queue.popleft()
        for u in adj[v]:
            if color[u] == WHITE:
                color[u] = GRAY
                distance[u] = distance[v] + 1
                parent[u] = v
                queue.append(u)
        color[v] = BLACK

    return color, distance, parent

