

def tsp_dynamic_programming(matrix, start = 0):
    n = len(matrix)
    if n == 0:
        return [], 0
    if start < 0 or start >= n:
        return [], 0
    if n == 1:
        return [start], 0

    INF = float('inf')
    subsets = 1 << n
    dp = [[INF] * n for _ in range(subsets)]
    dp[1 << start][start] = 0

    for mask in range(subsets):
        for i in range(n):
            if not (mask & (1 << i)):
                continue
            prev_mask = mask ^ (1 << i) # exclude city i from the mask
            for j in range(n):
                if prev_mask & (1 << j):
                    dp[mask][i] = min(dp[mask][i], dp[prev_mask][j] + matrix[j][i])

    full_mask = (1 << n) - 1
    min_cost = INF
    last_city = -1
    for i in range(n):
        if i == start:
            continue
        cost = dp[full_mask][i] + matrix[i][start]
        if cost < min_cost:
            min_cost = cost
            last_city = i

    if min_cost == INF:
        return [], 0

    tour = find_tour(matrix, dp, last_city, start)
    return tour, min_cost


def find_tour(matrix, dp, last_city, start):
    n = len(matrix)
    mask = (1 << n) - 1
    tour = [last_city]

    while mask != (1 << start):
        current = tour[-1]
        prev_mask = mask ^ (1 << current)
        for j in range(n):
            if prev_mask & (1 << j) and dp[mask][current] == dp[prev_mask][j] + matrix[j][current]:
                tour.append(j)
                mask = prev_mask
                break

    tour.reverse()
    tour.append(start)
    return tour

