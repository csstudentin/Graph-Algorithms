import heapq


def diskstra(adj, source):
    """
    Dijkstra algorithm to find shortest paths from source on non negative weighted graph
    Using Array
    adj: adjacency list
    source: source node
    """
    n = len(adj)
    if n <= 1 or source < 0 or source >= n:
        return None
    INF = float('inf')

    selected = [False] * n
    distance = [INF] * n
    parent = [-1] * n # -1 no parent
    distance[source] = 0

    for _ in range(n):
        u = -1
        min_dist = INF
        # Find the unselected vertex with smallest distance
        for v in range(n):
            if not selected[v] and distance[v] < min_dist:
                min_dist = distance[v]
                u = v
        if u == -1:
            break

        selected[u] = True
        # relax all neighbors of u
        for v, w in adj[u]:
            if not selected[v]:
                dist = distance[u] + w
                if dist < distance[v]:
                    distance[v] = dist
                    parent[v] = u

    return distance, parent


def dijkstra_heap(adj, source):
    """
    Dijkstra algorithm to find shortest paths from source on non negative weighted graph
    Using heap
    adj: adjacency list
    source: source node
    """
    n = len(adj)
    if n <= 1 or source < 0 or source >= n:
        return None
    INF = float('inf')

    selected = [False] * n
    distance = [INF] * n
    parent = [-1] * n # -1 no parent

    distance[source] = 0
    heap = [(0, source)] # (key, node)

    while heap:
        d, u = heapq.heappop(heap)
        if selected[u]:
            continue
        if d != distance[u]:
            continue
        selected[u] = True
        # relax all neighbors of u
        for v, w in adj[v]:
            new_distance = d + w
            if not selected[v] and new_distance < distance[v]:
                distance[v] = new_distance
                parent[v] = u
                heapq.heappush(heap, (new_distance, v))
    
    return distance, parent

