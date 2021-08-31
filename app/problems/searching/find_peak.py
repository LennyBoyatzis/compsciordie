# Time = O(log(n))
# Space = O(1)
def find_peak_iterative_binary_search(array):
    """Finds peak index using iterative binary search"""
    left, right = 0, len(array) - 1

    while left < right:
        mid = (left + right) // 2

        if array[mid] > array[mid+1]:
            right = mid
        else:
            left = mid + 1

    return left


# Time = O(log(n))
# Space = O(log(n)) height of call stack
def find_peak_recursive_binary_search(array):
    """Finds peak index using recursive binary search"""

    def search(nums, left, right):
        if left == right:
            return left

        mid = (left + right) // 2

        if nums[mid] > nums[mid+1]:
            return search(nums, left, mid)

        return search(nums, mid + 1, right)

    return search(array, 0, len(array) - 1)

# Time = O(n)
# Space = O(1)
def find_peak_linear_scan(array):
    size = len(array)

    for i in range(size-1):
        if array[i] > array[i+1]:
            return i

    return size - 1



if __name__ == '__main__':
    # array = [0, 1, 2, 3, 4, 3, 2, -1]
    array = [0, 10, 9, 8, 4, 3, 0]

    peak_idx = find_peak_iterative_binary_search(array)
    print(f'peak_idx {peak_idx}')

    peak_idx = find_peak_recursive_binary_search(array)
    print(f'peak_idx {peak_idx}')

    peak_idx = find_peak_linear_scan(array)
    print(f'peak_idx {peak_idx}')
