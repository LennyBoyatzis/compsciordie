def bisect_left(nums, target):
    """Returns the index of left insertion position for a target"""
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        mid_val = nums[mid]

        if mid_val < target:
            left = mid + 1
        else:
            right = mid

    if left < len(nums) and nums[left] == target:
        return left

    return -1


def bisect_right(nums, target):
    """Returns the index to the right insertion position for a target"""
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        mid_val = nums[mid]

        if mid_val <= target:
            left = mid + 1
        else:
            right = mid

    if nums[right - 1] == target:
        return right - 1

    return -1


def search_range(nums, target):
    left_idx = bisect_left(nums, target)
    right_idx = bisect_right(nums, target)

    return [left_idx, right_idx]


if __name__ == '__main__':
    nums = [2, 2, 2, 8, 8, 8, 8, 9, 10, 11]
    target = 8
    result = search_range(nums, target)
    print(f'result {result}')
