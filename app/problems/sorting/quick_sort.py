# N is length of input array

# Best Case Time O(nlog(n)) | Best Case Space O(log(n))
# Average Case Time O(nlog(n)) | Average Case Space O(log(n))
# Worst Case Time O(n^2) | Worst Case Space O(log(n))

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def recurse(array, start, end):
    if start >= end:
        return

    pivot = start 
    left = start + 1
    right = end

    while left <= right:
        pivot_val = array[pivot]
        left_val = array[left]
        right_val = array[right]

        if left_val > pivot_val and right_val < pivot_val:
            swap(array, left, right)

        if left_val < pivot_val:
            left += 1

        if right_val > pivot_val:
            right -= 1

    swap(array, right, pivot)
    left_subarray_is_smaller = right - 1 - start < end - (right + 1)

    if left_subarray_is_smaller:
        recurse(array, start, right-1)
        recurse(array, right+1, end)
    else:
        recurse(array, right+1, end)
        recurse(array, start, right-1)


def quick_sort(array):
    left, right = 0, len(array) - 1
    recurse(array, left, right)
    return array


if __name__ == '__main__':
    array = [8, 5, 2, 9, 5, 6, 3]
    res = quick_sort(array)

    print(f'array {array}')
