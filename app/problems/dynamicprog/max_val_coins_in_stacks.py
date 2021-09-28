def find_max_value(n, stacks):
    num_stacks = len(stacks)
    dp = [[0 for _ in range(num_stacks)] for _ in range(n)]
    dp[0][0] = stacks[0][0]

    # Prefil the first row
    for j in range(1, num_stacks):
        dp[0][j] = max(stacks[0][j], dp[0][j-1])

    # Prefil the first col
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + stacks[i][0]

    print(f'what is the dp {dp}')

    # Prefil the rest of the vals
    for i in range(1, n):
        for j in range(1, num_stacks):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j] + stacks[i][j])

    print(f'dp {dp}')
    return dp[-1][-1]


if __name__ == '__main__':
    stacks = [
        [10, 2, 11],
        [4, 2, 4],
        [1, 40, 1]]

    N = 3
    res = find_max_value(N, stacks)
    print(f'res {res}')
