from collections import defaultdict


def next_greatest_elements(nums1, nums2):
    stack = []
    store = defaultdict(int)

    for num in nums2:
        while stack and num > stack[-1]:
            top = stack.pop()

            if num not in store:
                store[top] = num
        if not stack or num < stack[-1]:
            stack.append(num)

    return [store[num] if num in store else -1 for num in nums1]


if __name__ == '__main__':
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    result = next_greatest_elements(nums1, nums2)
    print(f'result -> {result}')
