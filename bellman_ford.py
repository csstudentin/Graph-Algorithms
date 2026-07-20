

def bellman_ford(edges, n, source):
    """
    Bellman Ford algorithm to find shortest path from source
    edges: edge list (vertex u, vertex v, weight w)
    n: number of nodes
    source: source node
    """
    if not edges or n <= 1:
        return None
    if source < 0 or source >= n:
        return None
    INF = float('inf')

    distance = [INF] * n # all edges distance from source
    parent = [-1] * n # -1 no parent
    distance[source] = 0

    # Relax nodes |V| -1 times
    for _ in range(n-1):
        updated = False
        for u, v, w in edges: # u -> v
            if distance[v] != INF and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                parent[v] = u
                updated = True
        if not updated:
            break # break if no update

    # Detect negative cycle
    negative_cycle_flag = False
    for u, v, w in edges:
        if distance[v] != INF and distance[u] + w < distance[v]:
            negative_cycle_flag = True
            break
    
    return distance, parent, negative_cycle_flag


