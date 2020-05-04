from collections import Counter, defaultdict


def sliding_window(s, t):
    count_t = Counter(t)
    s_counts = defaultdict(int)
    complete_chars = 0 # must reach len(t)


if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    res = sliding_window(S, T)
    print(f'res {res}')
