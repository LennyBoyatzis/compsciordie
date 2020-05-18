from collections import defaultdict


def two_sum(nums, target):
    complements = defaultdict(list)

    for index, x in enumerate(nums):
        y = target - x

        if x in complements:
            idx, x = complements[x]
            return [idx, index]
        complements[y].extend([index, x])


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f'result {result}')
