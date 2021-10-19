import numpy as np


def get_adjacent_cells(row, col, array):
    n_rows, n_cols = len(array), len(array[0])
    offsets = [-1, 1]
    cells = []

    for c_off in offsets:
        a_col = col + c_off
        if 0 <= a_col < n_cols:
            if array[row][a_col] != 1:
                cells.append((row, a_col))
    return cells


def waterfall_streams(array, source):
    n_rows, n_cols = len(array), len(array[0])
    start_cell = (0, source)
    curr_row = 0

    def traverse(row, col, prev_row, percentage):
        cell_value = array[row][col]
        array[row][col] = percentage + cell_value

        if row == len(array) - 1:
            return

        if cell_value == 0 and array[row+1][col] != 1:
            traverse(row+1, col, row, percentage)
        else:
            neighbours = get_adjacent_cells(row, col, array)

            for neighbour in neighbours:
                n_r, n_c = neighbour
                if prev_row == row:
                    traverse(n_r, n_c, row, percentage/len(neighbours))
                else:
                    traverse(n_r, n_c, row, percentage/2)
    traverse(0, source, 0, 100)

    print(f'{np.matrix(array)}')
    return array


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
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    ans = [25, 0, 12.5, 0, 0, 0, 12.5, 6.25, 0, 3.125, 0, 0, 3.125, 37.5]

    # array = [
    #     [0, X, X, X, X, X, X, X, X, X, X, X, X, 0],
    #     [0, X, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, X, 0],
    #     [0, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, X, X],
    #     [0, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, X, 1, X],
    #     [X, X, X, X, X, 0, 0, 0, 0, X, X, X, X, X],
    #     [X, 1, 1, 1, X, 0, 0, 0, 0, X, 1, 1, 1, X],
    #     [X, 0, X, X, X, X, X, X, X, X, 0, 0, 0, X],
    #     [X, 0, X, 1, 1, 1, X, X, 1, 1, 1, 0, 0, X],
    #     [X, 0, X, 0, 0, X, X, X, X, 0, 0, 0, 0, X],
    #     [X, 1, X, 0, X, X, 1, 1, X, X, 1, 1, 0, X],
    #     [X, 0, X, 0, X, 1, 0, 0, 1, X, 0, 0, 0, X],
    #     [X, 0, X, 0, X, 0, 0, 0, 0, X, 0, 0, 0, X]]

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

    source = 3 
    res = waterfall_streams(array, source)
    # print(f'res {res}')
