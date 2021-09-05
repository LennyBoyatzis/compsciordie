def simple_binary_search(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def simple_binary_search_recursion(array, target, left, right):
    def search(array, target, left, right):
        if left == right:
            return left

        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return simple_binary_search_recursion(array, target, left, mid)
        else:
            return simple_binary_search_recursion(array, target, mid, right)

    return search(array, 0, len(array)-1)


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6]
    target = -6 
    target_idx = simple_binary_search(array, target)
    print(f'target_idx {target_idx}')
