def merge_sorted_arrays(a1, a2):
    merged = []
    p1, p2 = 0, 0

    while p1 < len(a1) and p2 < len(a2):
        if a1[p1] < a2[p2]:
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
    if len(array) == 1:
        return array

    mid = len(array) // 2

    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    merged = merge_sorted_arrays(left, right)
    return merged


if __name__ == '__main__':
    array = [10, -2, 12, 11, 6, 21, 19, 4, 8]
    ans = merge_sort(array)
    print(f'ans {ans}')
