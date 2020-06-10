from collections import deque

GATE = 0
WALL = -1
INF = 2147483647


def find_gates(rooms):
    m, n = len(rooms), len(rooms[0])
    gates = []

    for row in range(m):
        for col in range(n):
            room = rooms[row][col]
            if room == GATE:
                gates.append((row, col, 0))
    return gates


def get_neighbours(cell, rooms):
    m, n = len(rooms), len(rooms[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    adj_cells = [(cell[0]+v_off, cell[1]+h_off) for v_off, h_off in directions]
    valid_cells = []

    for cell in adj_cells:
        r, c = cell
        if (0 <= r < m) and (0 <= c < n) and rooms[r][c] == INF:
            valid_cells.append(cell)

    return valid_cells


def walls_and_gates(rooms):
    if not rooms:
        return

    gates = find_gates(rooms)
    queue = deque(gates)
    visited = set()

    while queue:
        gate = queue.pop()
        row, col, dist = gate

        if (row, col) not in visited:
            visited.add((row, col))
            rooms[row][col] = dist
            neighbs = get_neighbours((row, col), rooms)

            for neigh in neighbs:
                r, c = neigh
                queue.appendleft((r, c, dist+1))


if __name__ == '__main__':
    grid = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647]]

    result = walls_and_gates(grid)

    print(f'grid {grid}')
