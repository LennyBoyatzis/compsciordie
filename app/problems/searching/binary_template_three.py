"""
Keep Track of the Mid - 1, Mid, Mid + 1 elements
"""

def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left + 1 < right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    print(f'left -> {left}')
    print(f'right -> {right}')
    if nums[left] == target:
        return left
    elif nums[right] == target:
        return right

    return -1


if __name__ == '__main__':
    # Goal is the find peak
    target = 9 
    nums = [1, 2, 3, 5, 6, 7, 8, 9]
    res = binary_search(nums, target)
    print(f'result {res}')
