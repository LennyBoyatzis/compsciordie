def get_row_elements(board, row_idx):
    return set(board[row_idx])


def get_col_elements(board, col_idx):
    cols = set()
    for i in range(len(board)):
        col.add(board[i][0])

    return cols


def get_grid_elements(board, cell):
    r, c = cell
    grid_idx = (r + c) // 3



def solve_sudoku(board):
    """
    Overall idea
    -> For any given 0 value on the board, there are a set of feasible values
    which can be tried
    -> These feasible values are obtained by taking difference of the set{1-9} and then get
    all non-zero values in the same row, column and 3x3 grid
    -> The remaining feasible values, could be tried by looping through them
    and calling a recursive function
    """
    pass



if __name__ == '__main__':
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    ans = solve_sudoku(board)
    print(f'ans {ans}')
