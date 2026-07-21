"""
Greedy Heuristics
Solve TSP using MST and DFS
Use Prim's algorithm for mst
"""

def prim_mst(matrix, start = 0):
    n = len(matrix)
    if n <= 1:
        return []
    if start < 0 or start >= n:
        return []
    
    visited = [False] * n
    key = [float('inf')] * n  # minimum distance of node from mst 
    parent = [-1] * n 
    
    key[start] = 0
    
    for _ in range(n):
        # Find the unvisited vertex with the smallest key value
        u = -1
        best = float('inf')
        for v in range(n):
            if not visited[v] and key[v] < best:
                best = key[v]
                u = v
        
        if u == -1: # no vertex
            break
        
        visited[u] = True # added node to mst
        
        # Update key and parent for all unvisited neighbors
        for v in range(n):
            if not visited[v] and matrix[u][v] < key[v]:
                key[v] = matrix[u][v]
                parent[v] = u
    
    # Build list of MST edges (parent, child, weight)
    mst_edges = []
    for v in range(n):
        if v == start:
            continue
        u = parent[v]
        if u != -1:
            mst_edges.append((u, v, matrix[u][v]))
    return mst_edges


def build_directed_adjacency_list(edges, n):
    adj = [[] for _ in range(n)]
    for u, v, _ in edges:
        adj[u].append(v)
    return adj

# Double MST
def tsp_double_mst(matrix, start = 0):
    n = len(matrix)
    if n == 0:
        return [], 0
    if n == 1:
        return [start], 0
    if start < 0 or start >= n:
        return [], 0

    # 1. Build MST (Prim)
    mst_edges = prim_mst(matrix, start)

    # 2. Build directed adjacency list
    adj = build_directed_adjacency_list(mst_edges, n)

    # 3. Iterative preorder DFS starting from root start
    preorder = []
    stack = [start]
    while stack:
        u = stack.pop()
        preorder.append(u)

        for v in adj[u]:
            stack.append(v)

    tour = preorder + [start]
    total_cost = calculate_cost(tour, matrix)
    return tour, total_cost


def calculate_cost(tour, matrix):
    n = len(tour)
    if n <= 1:
        return 0
    cost = 0
    for i in range(1, n):
        cost += matrix[tour[i-1]][tour[i]]
    return cost
