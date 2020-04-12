"""
1 - starting square
2 - ending square
0 - empty square
-1 - obstacle
"""


def find_start(grid):
    """
    time: O(n * m)
    """
    START = 1
    n_rows = len(grid)
    n_cols = len(grid[0])

    for i in range(n_rows):
        for j in range(n_cols):
            cell = grid[i][j]
            if cell == START:
                return (i, j)


def get_neighbours(cell, grid):
    n_rows, n_cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbours = [(cell[0]+vert, cell[1]+hori) for vert, hori in directions]

    return list(filter(lambda cell: (0 <= cell[0] < n_rows and 0 <= cell[1] < n_cols),
                       neighbours))


def unique_paths_III(grid):
    EMPTY, GOAL = 0, 2
    paths = []
    start = find_start(grid)

    def backtrack(cell, path=set()):
        if cell not in path:
            path.add(cell)
            i, j = cell
            cell_val = grid[i][j]
            if cell_val == GOAL:
                paths.add(path)
            for neighbour in get_neighbours(cell, grid):
                row, col = neighbour
                val = grid[row][col]
                if val == GOAL:
                    paths.append(path)
                elif val == EMPTY:
                    backtrack(neighbour, path)

    backtrack(start)
    return len(paths)


if __name__ == '__main__':
    grid = [
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 2, -1]]
    result = unique_paths_III(grid)
    print(f'result {result}')
