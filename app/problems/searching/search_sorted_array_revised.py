
# target = 0 (6)
# [3, 4, 5, 6, 8, 12, 0, 1]
# [L, -, -, M, -, - , -, R]
# [-, -, -, -, -, - , L/M, R]

# target = 4 (1)
# [3, 4, 5, 6, 8, 12, 0, 1]
# [L, -, -, M, -, - , -, R]
# [L, M, R, -, -, - , -, -]

def search_sorted_array(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        left_val, mid_val, right_val = array[left], array[mid], array[right]

        if mid_val == target:
            return mid

        # LHS sorted
        if left_val < mid_val:
            if left_val <= target < mid_val:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if mid_val < target <= right_val:
                left = mid + 1
            else:
                right = mid - 1
    return -1


if __name__ == '__main__':
    target = 3 
    array = [3, 4, 5, 6, 8, 12, 0, 1]
    res = search_sorted_array(array, target)
    print(f'res {res}')
