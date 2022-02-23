def get_max_gold(grid):
    n_rows, n_cols = len(grid), len(grid[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(r, c):
        if r < 0 or r == n_rows or c < 0 or c == n_cols or grid[r][c] == 0:
            return 0

        path_sum = 0
        gold_val = grid[r][c]

        grid[r][c] = 0

        for r_off, c_off in directions:
            path_sum = max(path_sum, dfs(r+r_off, c+c_off))

        grid[r][c] = gold_val
        return path_sum + grid[r][c]

    ans = 0

    for r in range(n_rows):
        for c in range(n_cols):
            ans = max(ans, dfs(r, c))
    return ans


if __name__ == '__main__':
    grid = [
        [1,0,7],
        [2,0,6],
        [3,4,5],
        [0,3,0],
        [9,0,20]
    ]

    ans = get_max_gold(grid)
    print(f'ans {ans}')
    assert ans == 28
