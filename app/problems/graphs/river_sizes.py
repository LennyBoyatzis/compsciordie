from typing import Tuple, List
from collections import deque

RIVER = 1
LAND = 0

Cell = Tuple[int, int]
Grid = List[List[int]]
Sizes = List[int]
History = set()


def get_adjacent_cells(cell: Cell, grid: Grid) -> List[Cell]:
    """Returns valid adjacent cells for given cell"""
    row_bound, col_bound = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    valid_adjacent_cells = []

    for offset in directions:
        neighbour = (cell[0] + offset[0], cell[1] + offset[1])
        if 0 <= neighbour[0] < row_bound and 0 <= neighbour[1] < col_bound:
            valid_adjacent_cells.append(neighbour)
    return valid_adjacent_cells


def measure_river(start: Cell, grid: Grid, visited) -> int:
    """Performs BFS to measure the river size"""
    queue = deque([start])
    count = 0

    while queue:
        node = queue.pop()
        r, c = node
        cell_val = grid[r][c]
        if cell_val == RIVER and node not in visited:
            visited.add(node)
            count += 1
            neighbours = get_adjacent_cells(node, grid)

            for neighbour in neighbours:
                queue.appendleft(neighbour)
    return count


def explore_grid(grid: Grid) -> Sizes:
    """Counts sizes of all rivers located within a grid"""
    n_rows, n_cols = len(grid), len(grid[0])
    river_sizes = []
    visited = set()
    count_rivers = 0

    for i in range(n_rows):
        for j in range(n_cols):
            cell = (i, j)
            cell_val = grid[i][j]
            if cell not in visited and cell_val == RIVER:
                count_rivers += 1
                size = measure_river(cell, grid, visited)
                river_sizes.append(size)
    return river_sizes


if __name__ == '__main__':
    grid = [
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 1]]

    river_sizes = explore_grid(grid)
    print(f'river_sizes {river_sizes}')

    # neighbours = get_adjacent_cells((1, 3), grid)
    # print(f'neighbours {neighbours}')
