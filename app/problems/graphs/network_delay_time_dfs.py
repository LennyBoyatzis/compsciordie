from collections import defaultdict

"""
N - number of nodes
E - length of the times array (number of edges)

Time Complexity:
    - O (N^N + E log E)
    - Can visit each node up to N - 1 times, one per each other node
        -> N^N
    - We also have to explore every other edge and sort them
        -> E log E

Space Complexity:
    - O (N + E)
    - Size of graph is O(E)
    - Size of the implicit call stack is O(N)
"""


def network_delay_time(times, N, K):
    graph = defaultdict(list)

    for u, v, w in times:
        graph[u].append((w, v))

    dist = {node: float('inf') for node in range(1, N+1)}

    def dfs(node, elapsed):
        if elapsed >= dist[node]:
            return

        dist[node] = elapsed

        for time, child in sorted(graph[node]):
            dfs(child, elapsed + time)

    dfs(K, 0)
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
