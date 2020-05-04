def find_unsorted_subarray_brute(nums):
    """
    time: O(n2)
    space: O(1)
    """
    n = len(nums)
    left, right = n-1, 0

    for i in range(n):
        for j in range(i+1, n):
            if nums[j] < nums[i]:
                left = min(left, i)
                right = max(right, j)

    return max(0, right - left + 1)


def find_unsorted_subarray_sorting(nums):
    """
    time: O(nlog(n))
    space: O(1)
    """
    n = len(nums)
    left, right = n - 1, 0

    nums_sort = sorted(nums)

    for i in range(n):
        if nums[i] != nums_sort[i]:
            left = min(left, i)
            right = max(right, i)

    return max(0, right - left + 1)


def find_unsorted_subarray_stack(nums):
    """
    time: O(n)
    space: O(n)
    """
    stack = []

    for index, num in enumerate(nums):



if __name__ == '__main__':
    nums = [2, 6, 4, 8, 10, 9, 15]
    result = find_unsorted_subarray_sorting(nums)
    print(f'what is result {result}')
