def calc_sums(matrix):
    n_rows, n_cols = len(matrix), len(matrix[0])
    dp = [[0 for i in range(n_cols)] for j in range(n_rows)]

    dp[0][0] = matrix[0][0]

    # Prefil first column
    for i in range(1, n_rows):
        dp[i][0] = dp[i-1][0] + matrix[i][0] 

    # Prefil first row
    for j in range(1, n_cols):
        dp[0][j] = dp[0][j-1] + matrix[0][j]

    # Cal sums
    for i in range(1, n_rows):
        for j in range(1, n_cols):
            dp[i][j] = matrix[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] 

    return dp

def max_sum_submatrix(matrix, size):

    sums = calc_sums(matrix)
    print(f'sums {sums}')


if __name__ == '__main__':
    matrix = [
        [5, 3, -1, 5],
        [-7, 3, 7, 4],
        [12, 8, 0, 0],
        [1, -8, -8, 2]]
    size = 2
    res = max_sum_submatrix(matrix, size)
    # print(f'res {res}')
