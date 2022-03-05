def merge(a1, a2):
    """Merge 2 sorted arrays of different lengths into sorted order"""
    merged = []
    p1, p2 = 0, 0

    while p1 < len(a1) and p2 < len(a2):
        if a1[p1] <= a2[p2]:
            merged.append(a1[p1])
            p1 += 1
        else:
            merged.append(a2[p2])
            p2 += 1

    if p1 < len(a1):
        merged.extend(a1[p1:])

    if p2 < len(a2):
        merged.extend(a2[p2:])

    return merged


def merge_sort(array):
    """Merge sort algorithm"""
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left = merge_sort(array[:mid]) # Divide LHS
    right = merge_sort(array[mid:]) # Divide RHS

    combined = merge(left, right)
    return combined


if __name__ == '__main__':
    arr = [20, 14, 12, 8, 7, 6, 19, 200, 14, 41]
    ans = merge_sort(arr)
    print(f'ans {ans}')
