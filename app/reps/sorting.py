def test_sorting():
    strs = ['aa', 'BB', 'zz', 'CC']
    print(sorted(strs)) # ['BB', 'CC', 'aa', 'zz']
    print(sorted(strs, reverse=True)) # ['zz', 'aa', 'CC', 'BB']


def test_sorting_custom():
    strs = ['ccc', 'aaaa', 'd', 'bb']
    print(sorted(strs, key=len)) # ['d', 'bb', 'ccc', 'aaaa']

    # Note, the value in the sorted output is not modified
    # The lambda is just used for determining mapping
    nums = [100, 200, 300, 400]
    print(sorted(nums, key=lambda x: x*-1)) # [400, 300, 200, 100]


def tuples():
    # Tuples are not technically immutable as you can have
    # complex types stored in them
    # These complex types can be manipulated
    # They can't change in size once created
    # Fixed len parcels of data
    tupey = (1, 2, [1, 2, 3])
    tupey[2].append(10) # 1, 2, [1, 2, 3, 10])


if __name__ == '__main__':
    test_sorting()
    test_sorting_custom()
