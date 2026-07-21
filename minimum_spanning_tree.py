import heapq
INF = float('inf')

# spanning tree for connected graph
def mst_prim(adj):
    # adj: adjacency list (vertex, weight)
    n = len(adj)
    if n == 0:
        return []
    selected = [False] * n
    parent = [-1] * n # -1 no parent
    key = [INF] * n
    # initial
    key[0] = 0 # start: 0
    min_heap = [(0, 0)] # (key, node)
    mst_edgesdges = []

    while min_heap:
        current_key, u = heapq.heappop(min_heap)
        if selected[u]:
            continue
        selected[u] = True
        if parent[u] != -1:
            # add to mst edges
            mst_edgesdges.append((parent[u], u, current_key))
        for v, w in adj[u]:
            # update key
            if not selected[v] and w < key[v]:
                key[v] = w
                parent[v] = u
                heapq.heappush(min_heap, (w, v))

    return mst_edgesdges


# kruskal
import disjoint_set_union as dsu


def mst_kruskal(edges, n):
    # edges: edge list (u, v, w)
    # n: number of nodes
    if len(edges) <= 1 or n <= 1:
        return []
    nodes = [dsu.Node(i) for i in range(n)]
    for v in range(n):
        dsu.make_set(nodes[v])
    
    edges.sort(key=lambda edge: edge[2]) # sort edges by weight
    mst_edges = []

    for u, v, w in edges:
        if dsu.find_set(nodes[v]) == dsu.find_set(nodes[u]):
            continue
        dsu.union_set(nodes[u], nodes[v])
        mst_edges.append((u, v, w))

    return mst_edges


