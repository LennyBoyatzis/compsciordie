# Guarantees search space of 1 (mid)
def binary_search_one(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return - 1


# Guarantees search space of 2 (mid, mid+1)
# Note right is set to len(array) because we need
# to find a target which could be at the very end
# this break things as we don't have access to mid+1 for the final loop
def binary_search_two(array, target):
    left, right = 0, len(array)

    while left < right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid
        else:
            left = mid + 1
    return -1


# Guarantees search space of 3 (mid-1, mid, mid+1)
# Same as template 2 with setting right to len(array)
def binary_search_three(array, target):
    left, right = 0, len(array)

    while left + 1 < right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid
        else:
            left = mid
    return -1


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 9 
    res = binary_search_one(array, target)
    print(f'res {res}')

    res = binary_search_two(array, target)
    print(f'res {res}')

    res = binary_search_three(array, target)
    print(f'res {res}')
