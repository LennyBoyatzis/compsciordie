def decimal_to_binary(num):
    """Converts number to a binary string"""
    if num <= 1:
        return str(num)
    else:
        return decimal_to_binary(num // 2) + decimal_to_binary(num % 2)


if __name__ == '__main__':
    res = decimal_to_binary(11)
    expected = '1011' 
    print(f'res {res}')
    assert res == expected 
