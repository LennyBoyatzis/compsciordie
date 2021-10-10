# Brute Force Recursive Solution
# Runtime = O(b^d)
# b = branching factor (max value in array)
# d = length of the input array
# Space = O(b*d)

def brute_force_min_num_jumps(array):
    min_jumps = float('inf')

    def find_paths(i, num_jumps):
        nonlocal min_jumps

        if i >= len(array) - 1:
            min_jumps = min(min_jumps, num_jumps)
            return

        jumps = array[i]

        for jump in range(1, jumps+1):
            find_paths(i+jump, num_jumps+1)

    find_paths(0, 0)
    return min_jumps


# Runtime O(n^2)
# Space O(n)

def dp_min_num_jumps(array):
    jumps = [float('inf') for _ in range(len(array))]
    jumps[0] = 0

    for i in range(len(array)):
        for j in range(i):
            jump_size = array[j]
            # Can we jump from j to i?
            if j + jump_size >= i:
                jumps[i] = min(jumps[i], jumps[j] + 1)
    
    return jumps[-1]


# At each index we know what the max reach is
def min_num_jumps(array):
    pass

    


if __name__ == '__main__':
    array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
    result = min_num_jumps(array) # ['X', 'Y', 'Z', 'W']
    print(f'result {result}')
