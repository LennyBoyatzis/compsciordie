def find_peak(nums):
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid+1]:
            right = mid
        else:
            left = mid + 1

    return right


if __name__ == '__main__':
    array = [1,2,1,3,5,6,4]
    res = find_peak(array)
    print(f'res {res}')
