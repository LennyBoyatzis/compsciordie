# val, weight

#       0  1  2  3  4  5  6  7  8  9  10
# [   ] 0  0  0  0  0  0  0  0  0  0   0
# [1,2] 0
# [4,3] 0
# [5,6] 0
# [6,7] 0

# Given items, what is max value i can fit?

#             10
#         /  /  |  \
#        2  3   6  7

# Are the items sorted in any way?

def knapsack_prob_bf(items, capacity):
    max_val = float('-inf')

    def recurse(capacity, path_value):
        nonlocal max_val

        if capacity <= 0:
            max_val = max(max_val, path_value)
            return

        for item in items:
            value, weight = item[0], item[1]
            if weight <= capacity:
                recurse(capacity-weight, value+path_value)

    recurse(capacity, 0)
    return max_val


if __name__ == '__main__':
    items = [[1, 2], [4, 3], [5, 6], [6, 7]]
    capacity = 10
    res = knapsack_prob_bf(items, capacity)
    print(f'res {res}')
