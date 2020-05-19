from collections import defaultdict


def two_sum(nums, target):
    pairs = defaultdict(int)

    for index, x in enumerate(nums):
        y = target - x

        if x in pairs:
            idx = pairs[x]
            return [idx, index]
        pairs[y] = index


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f'result {result}')
