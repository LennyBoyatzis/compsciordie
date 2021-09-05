"""
Keep Track of the Mid, Mid + 1 elements
"""

def binary_search(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == '__main__':
    # Goal is the find peak
    nums = [1, 2, 3, 5, 6, 7, 4, 3]
    res = binary_search(nums)
    print(f'result {res}')
