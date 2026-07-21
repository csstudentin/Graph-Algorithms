

def tsp_brute_force_recursive(matrix, start = 0):
    """
    Recursive Brute Force 
    matrxi: matrix of distance
    """
    n = len(matrix)
    if n == 0:
        return [], 0
    if n == 1:
        return [start], 0
    if start < 0 or start >= n:
        return [], 0
    
    visited = [False] * n
    visited[start] = True

    def dfs_backtrack(v):
        min_dist = float('inf')
        optimal_path = None

        for u in range(n):
            if not visited[u]:
                visited[u] = True
                dist, path = dfs_backtrack(u)
                total_dist = matrix[v][u] + dist

                if total_dist < min_dist: # update 
                    min_dist = total_dist
                    optimal_path = [v] + path
                # backtrack
                visited[u] = False

        if optimal_path is None: # all cities have been visited
            return matrix[v][start], [v, start]
                
        return min_dist, optimal_path

    # Start from city start
    min_cost, best_tour = dfs_backtrack(start)
    return best_tour, min_cost

