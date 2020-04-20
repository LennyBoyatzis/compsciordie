from collections import Counter


def contains_t(window, t):
    window_count, t_count = Counter(window), Counter(t)
    return len(t_count - window_count) == 0


def sliding_window(s, t):
    left, right = 0, 0
    min_window, min_window_size = '', float('inf')

    while right <= len(s):
        window = s[left:right]

        while contains_t(window, t):
            if len(window) <= min_window_size:
                min_window = window
                min_window_size = len(window)
            left += 1
            window = s[left:right]
        right += 1

    return min_window


if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    res = sliding_window(S, T)
    print(f'res {res}')
