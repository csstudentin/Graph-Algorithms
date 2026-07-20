
def floyd_warshall(dist):
    """
    Calculate all-pairs shortest paths using dynamic programming Floyd Warshall algorithm.
    """
    n = len(dist)
    if n <= 1:
        return dist, [0]

    INF = float('inf')
    D = [row[:] for row in dist] # dynammic programming table of distances
    P = [[-1] * n for _ in range(n)] # dynamic programming table of midpoints

    for i in range(n): # (optional)
        D[i][i] = 0

    for k in range(n):
        for i in range(n):
            if D[i][k] == INF:
                continue
            for j in range(n):
                if D[k][j] == INF:
                    continue
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k

    return D, P

def reconstruct_path(P, i, j):
    pass

