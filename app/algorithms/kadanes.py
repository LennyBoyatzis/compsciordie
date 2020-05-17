def kadanes(A):
    """Find max sum in subarray

    If Array has only positive integers
    -> Sum the entire array

    If Array has negative integers
    -> Use kadanes algorithm
    """
    size, max_sum = len(A), 0

    for i in range(size):
        max_sum = max(max_sum+A[i], 0)

    return max_sum


if __name__ == '__main__':
    A = [5, -3, 5]
    result = kadanes(A)
    print(f'result {result}')
