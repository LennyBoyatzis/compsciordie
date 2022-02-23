"""
[4, 5, 6, 7, 8, 1, 2, 3]
[L, -, -, M, -, -, -, R]
[-, -, -, -, -, -, -, -]

"""


def find_rotation(nums):
    """
    Returns the Peak + 1th element i.e. the first index after the rotation
    """
    left, right = 0, len(nums) - 1

    if nums[left] < nums[right]:
        return 0

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid+1]:
            return mid + 1
        elif nums[left] < nums[mid]:
            left = mid + 1
        else:
            right = mid - 1


if __name__ == '__main__':
    array = [4, 5, 6, 7, 8, 1, 2, 3]
    res = find_rotation(array)
    print(f'res {res}')

    array = [4, 5, 6, 7, 8, 9, 10, 3]
    res = find_rotation(array)
    print(f'res {res}')

    array = [10, 5, 6, 7, 8, 9]
    res = find_rotation(array)
    print(f'res {res}')
