def test_sets(set_two):
    set_one = {'AA', 'B'}
    set_one |= set_two
    print(f"union {set_one}")


if __name__ == '__main__':
    set_two = {'C'}
    result = test_sets(set_two)
    print(f'what is the result {result}')
