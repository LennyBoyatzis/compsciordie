from collections import defaultdict


def longest_sub_two_distinct(s):
    left, right = 0, 0
    size = len(s)
    max_len = float('-inf')
    count_map = defaultdict(int)

    while right <= size:
        window = s[left:right]
        right_char = window[-1]
        count_map[right_char] += 1

        if len(count_map) <= 2:
            if len(window) > max_len:
                max_len = len(window)
            right += 1
        else:
            left_char = s[left]
            count_map[left_char] -= 1
            if count_map[left_char] == 0:
                del count_map[left_char]
            left += 1

    return max_len if max_len is not float('-inf') else 0


if __name__ == '__main__':
    S = "ccaabbb"
    result = longest_sub_two_distinct(S)
    print(f'result -> {result}')
