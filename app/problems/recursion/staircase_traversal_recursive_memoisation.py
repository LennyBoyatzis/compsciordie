# Top Down Recursive Approach (Brute Force)
# O(b^d) where b is branching factor and d is depth of tree

# Top Down Recursive Approach (memoization)
# O(b*d) where b is branching factor and d is depth of tree

def count(amount, max_steps, cache):
    if amount in cache:
        return cache[amount]

    if amount < 0:
        return 0

    if amount == 0:
        return 1

    ways = 0

    for i in range(1, max_steps+1):
        ways += count(amount-i, max_steps, cache)

    cache[amount] = ways
    return ways


def staircase_traversal(height, max_steps):
    cache = {}
    return count(height, max_steps, cache)


if __name__ == '__main__':
    height = 4 
    max_steps = 2
    res = staircase_traversal(height, max_steps)
    print(f'res {res}')
