def find_max_value(n, stacks):
    num_stacks = len(stacks)

    dp = [[0 for _ in range(n)]
          for _ in range(num_stacks)]


    for i in range(len(stacks)):
        stack = stacks[i]

        for j in range(n):
            for k in range(min(j, len(stack))):
                dp[i+1][j] = max(dp[i+1][j], stacks[i][k] + dp[i][j-k]) 
    
    # result = float('-inf')

    # for i in range(n+1):
        # result = max(result, dp[num_stacks][i])

    # return result


if __name__ == '__main__':
    stacks = [
        [10, 2, 11, 12],
        [4, 2, 4, 1000],
        [1, 40, 1]]

    N = 3
    res = find_max_value(N, stacks)
    print(f'res {res}')
