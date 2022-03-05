def backtrack(n, row, cols, diags, anti_diags):
    """Performs backtracking to find the solution"""
    if row == n:
        return 1

    solutions = 0

    for col in range(n):
        curr_diag = row - col
        curr_anti_diag = row + col

        # If queen can't be placed
        if (col in cols
            or curr_diag in diags
            or curr_anti_diag in anti_diags):
            continue

        # "Add" the queen to the board
        cols.add(col)
        diags.add(curr_diag)
        anti_diags.add(curr_anti_diag)

        # Move on to the next row with the updated board state
        solutions += backtrack(n, row+1, cols, diags, anti_diags)

        # Remove the queen from the board since we have already explored all
        # valid paths
        cols.remove(col)
        diags.remove(curr_diag)
        anti_diags.remove(curr_anti_diag)
    return solutions


def n_queens(n):
    """Returns number of ways to place `n` queens on an nxn board"""
    return backtrack(n, 0, set(), set(), set())


if __name__ == '__main__':
    ans = n_queens(6)
    print(f'ans {ans}')
