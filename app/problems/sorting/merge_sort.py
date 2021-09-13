def merge(a1, a2):
    """Merge 2 sorted arrays of different lengths into sorted order"""
    merged = []
    size1, size2 = len(a1), len(a2)
    p1, p2 = 0, 0 

    while p1 < size1 and p2 < size2:
        if a1[p1] <= a2[p2]:
            merged.append(a1[p1])
            p1 += 1
        else:
            merged.append(a2[p2])
            p2 += 1

    if p1 <= size1 - 1:
        merged.extend(a1[p1:])

    if p2 <= size2 - 1:
        merged.extend(a2[p2:])

    return merged


def merge_sort(array):
    """Merge sort algorithm"""
    if len(array) == 1:
        return array

    start, end = 0, len(array)
    mid = start + end // 2 

    left = merge_sort(array[start:mid]) # Divide LHS
    right = merge_sort(array[mid:end]) # Divide RHS

    combined = merge(left, right)

    return combined


if __name__ == '__main__':
    a1 = [3, 9]
    a2 = [1, 5]
    res = merge(a1, a2)
    print(f'res {res}')

    array = [9, 3, 1, 5, 3, 7, 2]
    res = merge_sort(array)
    print(f'res {res}')

