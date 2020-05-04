def reverse(A, left, right):
    while left <= right:
        A[left], A[right] = A[right], A[left]
        right -= 1
        left += 1


def pancake_sort(A):
    n = len(A)
    ans = []

    for i in range(n):
        max_val = max(A[i:])
        max_idx = A.index(max_val)
        reverse(A, i, max_idx)
        ans.append(max_idx - i)

    return A[::-1], ans


if __name__ == '__main__':
    A = [3, 2, 4, 1]
    result, ans = pancake_sort(A)
    print(f'result {result}')
    print(f'ans {ans}')
