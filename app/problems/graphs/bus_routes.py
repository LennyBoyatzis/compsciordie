from collections import defaultdict, deque


def build_graph(routes):
    graph = defaultdict(list)
    for index, route in enumerate(routes):
        n = len(route)
        for i in range(n):
            stop = route[i]
            for j in range(n):
                if i != j:
                    graph[stop].append((index, route[j]))
    return graph


def num_buses_to_dest(routes, S, T):
    graph = build_graph(routes)
    # print(f'graph {graph}')
    visited = set()
    queue = deque([(set(), S)])

    while queue:
        bus_lines, stop_id = queue.pop()

        if stop_id not in visited:
            visited.add(stop_id)
            stops = graph[stop_id]

            for bus_line, stop_id in stops:
                if stop_id == T:
                    print(f'bus_lines {bus_lines}')
                    print(f'visited {visited}')
                    bus_lines.add(bus_line)
                    return len(bus_lines)

                if stop_id not in visited:
                    bus_lines.add(bus_line)
                    queue.appendleft((set(bus_lines), stop_id))

    return -1


if __name__ == '__main__':
    routes = [
        [1,9,12,20,23,24,35,38],
        [10,21,24,31,32,34,37,38,43],
        [10,19,28,37],
        [8],
        [14,19],
        [11,17,23,31,41,43,44],
        [21,26,29,33],
        [5,11,33,41],
        [4,5,8,9,24,44]]

    S, T = 37, 28
    result = num_buses_to_dest(routes, S, T)
    print(f'result -> {result}')
