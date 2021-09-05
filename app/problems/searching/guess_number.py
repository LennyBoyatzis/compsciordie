SECRET_NUMBER = 42

def guess(x):
    if x == SECRET_NUMBER:
        return 0
    elif SECRET_NUMBER > x:
        return 1
    else:
        return -1

def guess_number(n):
    left, right = 1, n

    while left <= right:
        mid = (left + right) // 2
        x = guess(mid)

        if x == 0:
            return mid
        elif x == 1:
            left = mid + 1
        else:
            right = mid - 1

    return right

if __name__ == '__main__':
    num_range = 100
    secret_num = guess_number(num_range)
    print(f'secret_num {secret_num}')
