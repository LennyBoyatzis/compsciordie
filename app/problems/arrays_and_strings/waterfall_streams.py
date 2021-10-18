def get_adjacent_cells(row, col, array, visited):
    n_rows, n_cols = len(array), len(array[0])
    offsets = [-1, 1]
    cells = []

    for c_off in offsets:
        a_col = col + c_off
        if 0 <= a_col < n_cols:
            if array[row][a_col] == 0 and (row, a_col) not in visited:
                cells.append((row, a_col))
    return cells


def waterfall_streams(array, source):
    n_rows, n_cols = len(array), len(array[0])
    start_cell = (0, source)
    fills = [0] * n_cols
    visited = set()
    curr_row = 0

    def traverse(row, col, prev_row, percentage):
        cell_value = array[row][col]
        if (row, col) in visited:
            return
        else:
            visited.add((row, col))

        if row == len(array) - 1:
            fills[col] = percentage
            return

        if cell_value == 0 and array[row+1][col] != 1:
            traverse(row+1, col, row, percentage)
        else:
            neighbours = get_adjacent_cells(row, col, array, visited)

            for neighbour in neighbours:
                n_r, n_c = neighbour
                if prev_row == row:
                    traverse(n_r, n_c, row, percentage)
                else:
                    traverse(n_r, n_c, row, percentage/2)
    traverse(0, source, 0, 100)
    return fills


if __name__ == '__main__':
    # array = [
    #     [0, 0, 0, 0, 0, 0, 0],
    #     [1, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 1, 1, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0],
    #     [1, 1, 1, 0, 0, 1, 0],
    #     [0, 0, 0, 0, 0, 0, 1],
    #     [0, 0, 0, 0, 0, 0, 0]]

    # Note this example demonstrates having to recombine forked streams
    # How should this be handled?

    array = [
        [0, X, X, X, X, X, X, X, X, X, X, X, X, 0],
        [0, X, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, X, 0],
        [0, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, X, X],
        [0, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, 1, X],
        [X, X, X, X, X, 0, 0, 0, 0, X, X, X, X, X],
        [X, 1, 1, 1, X, 0, 0, 0, 0, X, 1, 1, 1, X],
        [X, 0, X, X, X, X, X, 0, 0, X, 0, 0, 0, X],
        [X, 0, X, 1, 1, 1, X, 0, 1, 1, 1, 0, 0, X],
        [X, 0, X, 0, 0, X, X, X, X, 0, 0, 0, 0, X],
        [X, 1, X, 0, X, X, 1, 1, X, X, 1, 1, 0, X],
        [X, 0, X, 0, X, 1, 0, 0, 1, X, 0, 0, 0, X],
        [X, 0, X, 0, X, 0, 0, 0, 0, X, 0, 0, 0, X]]

    # array = [
    #     [0, 0, 0, X, 0, 0, 0],
    #     [1, X, X, X, X, X, 0],
    #     [0, X, 1, 1, 1, X, 0],
    #     [0, X, 1, X, X, X, 1],
    #     [X, X, 1, X, 1, 1, 0],
    #     [X, 1, X, X, X, 0, 0],
    #     [X, X, X, 1, X, X, 0],
    #     [X, X, 1, 0, 1, X, 0],
    #     [X, X, 0, 0, 0, X, 0]]

    # ans = [25, 6.25, 0, 0, 0, 6.25, 0]

    # array = [
    #     [0, 0, 0, 0, 0, 0, 0],
    #     [1, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 1, 1, 0, 0],
    #     [0, 0, 1, 0, 0, 0, 1],
    #     [0, 0, 1, 0, 1, 1, 0],
    #     [0, 1, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 1, 0, 0, 0],
    #     [0, 0, 1, 0, 1, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0]]

    source = 8 
    res = waterfall_streams(array, source)
    print(f'res {res}')
