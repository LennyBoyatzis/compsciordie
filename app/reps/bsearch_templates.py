def vanilla_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# [1, 2, 10, 6, 5, 4, 3, -40, -100]
# [-, -, L/R , -, -, -, -, -  ,  -  ]

# 5 > 4
# 10 > 6
# 2 > 10

def find_peak(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[mid+1]:
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == '__main__':
    target = 22 
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    res = vanilla_search(arr, target)
    print(f'res {res}')

    arr = [100, 12, 10, 6, 5, 4, 3, -40, -100]
    res = find_peak(arr)
    print(f'res {res}')

    arr = []
