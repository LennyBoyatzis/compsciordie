"""
- You have a table with M stacks of coins
- You are able to take N coins
- What is the max value you can take from the stacks

Stacks
stack_1 = [10, 14, 1]
stack_2 = [2, 2, 40]
stack_3 = [11, 4, 1]
"""


def find_max_value(stacks, N):
    """
    N - number of picks
    M - stacks of coins
    D - stack depth

    Time: O(M**N)
    Space: O(N) - Height of the recursive tree
    """
    max_val = 0
    stack_depth = len(stacks[0])

    def recurse(picks, stack_ptrs, curr_sum):
        nonlocal max_val

        # Base case: If you run out of picks
        if picks == 0:
            max_val = max(max_val, curr_sum)
            return

        for i in range(len(stacks)):
            if stack_ptrs[i] < len(stacks[i]):
                stack_ptrs_copy = stack_ptrs.copy()
                stack_ptrs_copy[i] += 1
                val = stacks[i][stack_ptrs[i]]
                recurse(picks-1, stack_ptrs_copy, curr_sum + val)

    stack_ptrs = [0] * len(stacks)
    recurse(N, stack_ptrs, 0)
    return max_val


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
