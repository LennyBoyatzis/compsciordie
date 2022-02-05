def greatest_common_divisor_itr(num1, num2):
    """Finds the largest positive integer that divides both numbers"""
    divisor = 1
    largest = 1

    while divisor <= min(num1, num2):
        if num1 % divisor == 0 and num2 % divisor == 0:
            largest = divisor
        divisor += 1

    return largest


def greatest_common_divisor_rec(num1, num2):
    """Finds the largest positive integer that divides both numbers"""
    # Base Case
    if num1 == num2:
        return num1

    # Recursive Case
    if num1 > num2:
        return greatest_common_divisor_rec(num1 - num2, num2)
    else:
        return greatest_common_divisor_rec(num1, num2 - num1)



if __name__ == '__main__':
    res = greatest_common_divisor(6, 9)
    print(f'res {res}')
    assert res == 3

    res = greatest_common_divisor(42, 56)
    print(f'res {res}')
    assert res == 14

    res = greatest_common_divisor(23, 23)
    print(f'res {res}')
    assert res == 23 
