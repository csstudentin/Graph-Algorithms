
def is_directed_acyclic_graph(adj):
    """
    check if a graph is directed acyclic graph using dfs three state color
    adj: adjacency list
    """
    n = len(adj)
    if n == 0:
        return True

    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n

    for start in range(n):
        if color[start] != WHITE:
            continue
        stack = [(start, False)]  # (node, is_processed)
        color[start] = GRAY

        while stack:
            u, is_processed = stack.pop()

            if not is_processed:
                stack.append((u, True))
                for v in adj[u]:
                    if color[v] == GRAY:
                        # cycle detected
                        # back edge
                        return False
                    if color[v] == WHITE:
                        color[v] = GRAY
                        stack.append((v, False))
            else:
                color[u] = BLACK
    return True

