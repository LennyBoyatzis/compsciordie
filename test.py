from collections import Counter

def is_subset(counts_sub_s, counts_t):
    diff = counts_t - counts_sub_s
    print(f'diff: {len(diff)}')
    return len(diff) == 0

def min_window(s: str, t: str) -> str:
    counts_sub_s = Counter()
    counts_t = Counter(t)
    min_size = float('inf')
    start, end = 0, 0
    min_start, min_end = 0, 0
    
    while end < len(s):
        next_char = s[end]
        counts_sub_s.update(next_char)
        
        while is_subset(counts_sub_s, counts_t):
            start_char = s[start]
            counts_sub_s[start_char] -= 1
            start += 1
            print(f'decreasing {s[start:end]}')
        
            if end-start < min_size:
                min_size = end-start
                min_start, min_end = start, end
        end += 1
        print(f'increasing {s[start:end]}')

    return "" if min_size == float('inf') else s[min_start:min_end]


if __name__ == '__main__':
    S = "BACCTFHK"
    # S = "BACCT"
    T = "CCTAF"

    counts_sub_s = Counter(S)
    counts_t = Counter(T)

    # test = is_subset(counts_sub_s, counts_t)
    # print(test)

    ans = min_window(S, T)
    print(f'ans -> {ans}')
    
