"""
- You have a table with M stacks of coins
- You are able to take N coins
- What is the max value you can take from the stacks

Stacks
stack_1 = [10, 14, 1]
stack_2 = [2, 2, 40]
stack_3 = [11, 4, 1]

Stack Sums (Prepend 0's)
stack_1 = [0, 10, 24, 25]
stack_2 = [0,  2,  4, 44]
stack_3 = [0, 11, 15, 16]
"""

def calc_stack_sums(stacks):
    sums = []
    for stack in stacks:
        prefix = [0]
        for coin in stack:
            prefix.append(prefix[-1]+coin)
        sums.append(prefix)
    return sums


def find_max_value(stacks, N):
    """
    N - number of picks
    M - stacks of coins
    D - stack depth

    Time: O(M * D * N)
    Space: O(N)
    """
    num_stacks = len(stacks) # Number of coin stacks
    num_picks = N # Number of coins you can take
    height = len(stacks[0]) # Height of each coin stack (assume equal size stacks)
    sums = calc_stack_sums(stacks)
    dp = [0]*(num_picks+1)

    for i in range(num_stacks):
        new_dp = [0]*(num_picks+1)
        for j in range(num_picks+1):
            for x in range(min(j, height)+1):
                new_dp[j] = max(new_dp[j], dp[j-x] + sums[i][x])
        dp = new_dp
    return dp[-1]


if __name__ == '__main__':
    stack_1 = [10, 14, 1]
    stack_2 = [2, 2, 40]
    stack_3 = [11, 4, 1]
    stacks = [
        stack_1,
        stack_2,
        stack_3
    ]
    N = 3 # (num coins you can take)
    res = find_max_value(stacks, N)
    print(f'res {res}')
    assert res == 44 # (2 + 2 + 40)

    N = 2
    res = find_max_value(stacks, N)
    print(f'res {res}')
    assert res == 24 # (10 + 14)
