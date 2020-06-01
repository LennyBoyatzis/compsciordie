from collections import defaultdict, deque


def calc_equation(equations, values, queries):
    graph = defaultdict(list)

    def build_graph(equations, values):
        for vertices, value in zip(equations, values):
            f, t = vertices
            graph[f].append((t, value))
            graph[t].append((f, 1/value))

    def find_path(query):
        b, e = query

        if b not in graph or e not in graph:
            return -1.0

        q = deque([(b, 1.0)])
        visited = set()

        while q:
            front, cur_product = q.popleft()
            if front == e:
                return cur_product
            visited.add(front)
            for neighbor, value in graph[front]:
                if neighbor not in visited:
                    q.append((neighbor, cur_product*value))

        return -1.0

    build_graph(equations, values)
    return [find_path(q) for q in queries]


if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    result = calc_equation(equations, values, queries)
    print(f'result {result}')
