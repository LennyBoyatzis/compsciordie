from collections import defaultdict


def build_graph(flights):
    graph = defaultdict(list)

    for (src, dst, cost) in flights:
        graph[src].append((dst, cost))

    return graph


def cheapest_flights(n, flights, src, dst, K):
    """
    Find cheapest price from source to destination with up to K stops
    """
    graph = build_graph(flights)


if __name__ == '__main__':
    n = 3
    edges = [
        [0, 1, 100],
        [1, 2, 100],
        [0, 2, 500]]
    src = 0
    dst = 2
    K = 1
    result = cheapest_flights(n, edges, src, dst, K)
    print(f'result {result}')
