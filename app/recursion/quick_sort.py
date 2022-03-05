def partition(array, lo, hi):
    """Finds pivot and returns its position in sorted array"""
    pivot = array[hi]
    i = lo

    for j in range(lo, hi):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[i], array[hi] = array[hi], array[i]
    return i


def qsort(array, lo, hi):
    """Helper recursive function"""
    if lo < hi:
        p = partition(array, lo, hi)
        qsort(array, lo, p - 1)
        qsort(array, p+1, hi)


def quick_sort(array):
    """Sorts array in ascending order"""
    size = len(array)
    qsort(array, 0, size-1)
    return array
    

if __name__ == '__main__':
    arr = [20, 14, 12, 8, 7, 6, 19, 200, 14, 41]
    ans = quick_sort(arr)
    print(f'ans {ans}')
