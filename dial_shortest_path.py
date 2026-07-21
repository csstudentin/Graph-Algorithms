from collections import deque

def dial_shortest_path(adj:list[list], source):
    """
    Dial's shortest path from source algorithm
    All weights must be non negative integer
    adj: adjacency list
    source: source node
    """
    n = len(adj)
    if n <= 1 or source < 0 or source >= n:
        return None
    
    count = 0 # count of needed new nodes
    for u in range(n):
        for v, w in adj[u]:
            if w > 1:
                w == w // 1
                count += w - 1

    new_n = n + count
    new_adj = [[] for _ in range(new_n)]
    next_node = n  # first new node index

    for u in range(n):
        for v, w in adj[u]:
            if w == 1:
                new_adj[u].append(v)
            else:
                # Create chain of w-1 intermediate nodes
                w == w // 1
                prev = u
                for _ in range(w - 1):
                    new_adj[prev].append(next_node)
                    prev = next_node
                    next_node += 1
                # Last intermediate connects to v
                new_adj[prev].append(v)

    # Run BFS on new adj
    dist, parent = bfs(new_adj, source)
    return dist[:n], parent[:n]


def bfs(adj, source):
    # bfs 
    # adj: adjacency list
    # source: source node
    n = len(adj)
    if n <= 1 or source < 0 or source >= n:
        return []
    INF = float('inf')

    visited = [False] * n
    distance = [INF] * n
    parent = [-1] * n # -1 no parent

    visited[source] = True
    distance[source] = 0
    queue = deque([source])

    while queue:
        u = queue.popleft() # dequeue

        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u
                queue.append(v)
    
    return distance, parent

