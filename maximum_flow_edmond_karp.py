from collections import deque


def edmond_karp(capacity, source, sink):
    """
    Compute maximum flow from source to sink using Edmond-Karp algorithm
    capacity: capacity matrix
    """
    n = len(capacity)
    if n <= 1:
        return None
    if source < 0 or source >= n:
        return None
    if sink < 0 or sink >= n:
        return None
    if source == sink:
        return None
    
    flow = [[0] * n for _ in range(n)] # flow matrix
    residual = [row[:] for row in capacity] # residual matrix
    maximum_flow = 0

    while True:
        # 1: find an augmenting path
        path = find_augmenting_path(residual, source, sink)
        if len(path) == 0:
            # no path
            break
        # 2: find bottleneck
        bottleneck = find_bottleneck(path, residual)
        # 3: update flow, residual matrix and maximum_flow
        update(path, residual, flow, bottleneck)
        maximum_flow += bottleneck

    return maximum_flow, flow, residual


def find_augmenting_path(residual, source, sink):
    # find augmenting path using BFS
    n = len(residual)

    def bfs():
        visited = [False] * n
        parent = [-1] * n # -1 no parent

        visited[source] = True
        queue = deque([source])

        while queue:
            u = queue.popleft() # dequeue
            for v in range(n):
                if v == sink and residual[u][v] > 0:
                    parent[sink] = u
                    return parent
                if not visited[v] and residual[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
        return parent

    parent = bfs()
    if parent[sink] == -1:
        # no augmenting path exists
        return []
    # find path using parent list
    path = []
    v = sink
    while v != -1:
        path.append(v)
        v = parent[v]
    path.reverse()

    return path
    

def find_bottleneck(augmenting_path, residual):
    # find bottleneck from augmenting path
    bottleneck = float('inf')
    n = len(augmenting_path)
    u = augmenting_path[0]

    for i in range(1, n):
        v = augmenting_path[i]
        bottleneck = min(bottleneck, residual[u][v])
        u = v

    return bottleneck


def update(augmenting_path, residual, flow, bottleneck):
    n = len(augmenting_path)
    
    u = augmenting_path[0]
    for i in range(1, n):
        v = augmenting_path[i]
        # update
        residual[u][v] -= bottleneck
        flow[u][v] += bottleneck

        residual[v][u] += bottleneck
        flow[v][u] -= bottleneck

        u = v




if __name__ == '__main__':
    # Graph with 4 nodes: 0→1 (3), 0→2 (2), 1→2 (1), 1→3 (2), 2→3 (3)
    capacity = [
        [0, 3, 2, 0],
        [0, 0, 1, 2],
        [0, 0, 0, 3],
        [0, 0, 0, 0]
    ]

    max_flow, flow, residual = edmond_karp(capacity, 0, 3)
    print(max_flow)  # Output: 5

