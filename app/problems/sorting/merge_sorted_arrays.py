# K arrays
# N is average length of the k arrays
# Space O(NK) (results list)
# Time (Onk log nk)
def brute_force_merge_sorted_arrays(arrays):
    """Merge multiple sorted arrays into 1 sorted array"""
    res = []

    for array in arrays:
        res.extend(array)

    res.sort()
    return res


def merge_sorted_arrays(arrays):
    pass


if __name__ == '__main__':
    arrays = [
        [1, 5, 9, 21],
        [-1, 0],
        [-124, 81, 121],
        [3, 6, 12, 20, 150]]
    res = merge_sorted_arrays(arrays)
    print(f'res {res}')
