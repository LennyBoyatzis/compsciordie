import heapq


def shortest_paths(graph, start):
    """
    Finds the short path to visit all nodes
    """
    pq = [(0, start)]
    shortest_paths = {}

    while pq:
        path_cost, node = heapq.heappop(pq)

        if node in shortest_paths:
            continue

        shortest_paths[node] = path_cost

        for child, cost in graph[node]:
            if child not in shortest_paths:
                heapq.heappush(pq, (path_cost + cost, child))

    return max(shortest_paths.values()) if len(shortest_paths) == len(graph) else -1


if __name__ == '__main__':
    graph = {
        'a': [('c', 3), ('b', 7)],
        'b': [('a', 7), ('c', 1), ('d', 2), ('e', 6)],
        'c': [('a', 7), ('b', 1), ('d', 2)],
        'd': [('c', 2), ('b', 2), ('e', 4)],
        'e': [('b', 6), ('d', 4)]}

    start = 'a'
    result = shortest_paths(graph, start)
    print(f'result {result}')
