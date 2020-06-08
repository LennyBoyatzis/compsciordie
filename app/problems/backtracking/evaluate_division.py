from collections import defaultdict, deque


def build_graph(equations, values):
    graph = defaultdict(list)

    for equation, value in zip(equations, values):
        top, bottom = equation
        graph[top].append((bottom, value))
        graph[bottom].append((top, 1/value))

    return graph


def find_path(graph, query):
    start, end = query

    if start not in graph or end not in graph:
        return -1.0

    if start == end:
        return 1.0

    queue = deque([(start, 1.0)])
    visited = set()

    while queue:
        node, cur_product = queue.pop()
        if node == end:
            return cur_product

        if node not in visited:
            visited.add(node)
            neighbours = graph[node]

            for neighbour, edge in neighbours:
                queue.appendleft((neighbour, cur_product * edge))

    return -1.0


def calc_equation(equations, values, queries):
    graph = build_graph(equations, values)
    return [find_path(graph, q) for q in queries]


if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    result = calc_equation(equations, values, queries)
    print(f'result {result}')
