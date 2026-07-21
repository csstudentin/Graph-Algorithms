
# topological sort for DAG graph
def topological_sort(adj):
    n = len(adj)
    if n == 0:
        return []
    visited = [False] * n
    order = []

    def dfs(s):
        stack = [(s, False)] # (node, finished_processing)
        while stack:
            v, is_finish = stack.pop()
            if not is_finish:
                if visited[v]: # already visited
                    continue
                visited[v] = True
                stack.append((v, True))
                for u in adj[v]:
                    if not visited[u]:
                        stack.append((u, False))
            else:
                order.append(v)

    for v in range(n):
        if not visited[v]:
            dfs(v)
    
    order.reverse()
    return order

