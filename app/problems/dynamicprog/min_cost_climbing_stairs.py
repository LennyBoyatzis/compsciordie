from functools import lru_cache

# Recursive Tree, at each level
# take either 1 step down or 2 steps down
# We can stop when we get to either step 0 or step 1

#        4 
#      /    \
#     3       2
#    / \     /  \
#   2   1    1    0 
#  / \ / \  / \
# 1  0 0 -1 0 -1

# Without Memoization
# Runtime O(2^n) -> O(b^d) where b is branching factor and d is depth of tree
# Space O(n)

# With Memoization
# We only need to calculate the min cost at each step once
# Runtime O(n)
# Space O(n)

# NOTE: You do not need to land evenly on the top stair
# The "top of the floor" does not refer to the final index of costs. 
# We actually need to "arrive" beyond the array's bounds.


def min_cost_climbing_stairs_recursion(costs):
    @lru_cache(maxsize=None)
    def climb(n):
        if n <= 1:
            return 0

        p1 = costs[n-1] + climb(n-1)
        p2 = costs[n-2] + climb(n-2)

        return min(p1, p2)
    return climb(len(costs))


# Runtime O(n)
# Space O(1)

def min_cost_climbing_stairs_dp(costs):
    p1 = p2 = 0 

    for i in range(2, len(costs) + 1):
        temp = p1
        p1 = min(p1 + costs[i-1], p2 + costs[i-2])
        p2 = temp

    return p1


if __name__ == '__main__':
    costs = [1, 2, 3, 4]
    res = min_cost_climbing_stairs_recursion(costs)
    print(f'res {res}')
