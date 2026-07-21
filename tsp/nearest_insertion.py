

def nearest_insertion(matrix, start=0):
    n = len(matrix)
    if n == 0:
        return [], 0
    if start < 0 or start >= n:
        return [], 0
    if n == 1:
        return [start], 0
    if n == 2:
        other = 1 - start
        tour = [start, other, start]
        return tour, calculate_cost(tour, matrix)

    # Pick initial two cities to form a 3‑city tour
    a = min((j for j in range(n) if j != start), key=lambda j: matrix[start][j])
    b = min((j for j in range(n) if j != start and j != a), key=lambda j: matrix[a][j])

    tour = [start, a, b]
    visited = [False] * n
    for city in tour:
        visited[city] = True

    # min_dist[x] = distance from x to the nearest city already in the tour
    min_dist = []
    for x in range(n):
        if visited[x]:
            min_dist.append(float("inf"))
        else:
            min_dist.append(min(matrix[x][c] for c in tour))

    while not all(visited):

        v = min((x for x in range(n) if not visited[x]), key=lambda x: min_dist[x])

        best_increase = float("inf")
        best_pos = 1

        for i in range(len(tour)):
            u = tour[i]
            w = tour[(i + 1) % len(tour)]
            increase = matrix[u][v] + matrix[v][w] - matrix[u][w]
            if increase < best_increase:
                best_increase = increase
                best_pos = i + 1

        tour.insert(best_pos, v)
        visited[v] = True

        # Update distances for the remaining unvisited cities
        for x in range(n):
            if not visited[x]:
                if matrix[x][v] < min_dist[x]:
                    min_dist[x] = matrix[x][v]

    tour.append(start)  # close the cycle
    return tour, calculate_cost(tour, matrix)


def calculate_cost(tour, matrix):
    n = len(tour)
    if n <= 1:
        return 0
    cost = 0
    for i in range(1, n):
        cost += matrix[tour[i-1]][tour[i]]
    return cost

