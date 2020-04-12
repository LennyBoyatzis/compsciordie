from collections import defaultdict

"""
Use Dijkstras Algorithm to find the shortest path for source to all targets

Dijkstra's Algo:
    - Shortest distance from one node to every other node in the graph

Time Complexity:
    - O(N^2)
"""


def network_delay_time(times, N, K):
    graph = defaultdict(list)

    for (u, v, w) in times:
        graph[u].append((v, w))

    dist = {node: float('inf') for node in range(1, N+1)}
    visited = set()
    dist[K] = 0

    while True:
        cand_node, cand_dist = -1, float('inf')
        for i in range(1, N+1):
            if i not in visited and dist[i] < cand_dist:
                cand_dist = dist[i]
                cand_node = i

        if cand_node < 0:
            break

        visited.add(cand_node)

        for child, time in graph[cand_node]:
            dist[child] = min(dist[child], dist[cand_node] + time)

    ans = max(dist.values())
    return ans if ans < float('inf') else -1


if __name__ == '__main__':
    N, K = 6, 2
    times = [
        [2, 1, 1],
        [1, 3, 1],
        [2, 4, 2],
        [4, 3, 4],
        [3, 5, 1],
        [4, 5, 2],
        [4, 6, 3]]

    result = network_delay_time(times, N, K)
    print(f'result {result}')
