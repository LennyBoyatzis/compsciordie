# 1 -> 1
# 2 -> 4
# 3 -> 9
# 4 -> 16
# 5 -> 25
# 6 -> 36

def sqrt(x):
    if x < 2:
        return 0

    left, right = 2, x // 2

    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid**2

        if mid_squared == x:
            return mid
        elif mid_squared > x:
            right = mid - 1
        else:
            left = mid + 1

    return right


if __name__ == '__main__':
    x = 16 
    res = sqrt(x)
    print(f'res -> {res}')
