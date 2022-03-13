"""
Best case runtime O(n log n)
- when we select a pivot which is the median at each step

Worst case runtime O(n2)
- when we select a max or min at each step

Space is constant O(1)
- Algorithm sorts elements in place
"""

def partition(nums, lo, hi):
    """Partitions array around pivot and returns pivot index"""
    pivot = nums[hi]
    i = lo

    for j in range(lo, hi):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[hi], nums[i] = nums[i], nums[hi]
    return i


def qsort(nums, lo, hi):
    if lo < hi:
        p = partition(nums, lo, hi)
        qsort(nums, lo, p-1)
        qsort(nums, p+1, hi)


def quick_sort(nums):
    qsort(nums, 0, len(array)-1)


if __name__ == '__main__':
    array = [10, -2, 12, 11, 6, 21, 19, 4, 8]
    ans = quick_sort(array)
    print(f'array {array}')
