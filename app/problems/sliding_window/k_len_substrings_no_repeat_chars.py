from collections import defaultdict


def num_k_len_substring_no_repeats(s, k):
    window_counts = defaultdict(int)
    ans, left, right = 0, 0, 0

    while right < len(s):
        window_counts[s[right]] += 1

        while window_counts[s[right]] > 1:
            window_counts[s[left]] -= 1
            left += 1

        if right - left + 1 == K:
            ans += 1
            window_counts[s[left]] -= 1
            left += 1

        right += 1
    return ans


if __name__ == '__main__':
    S = "havefunonleetcode"
    K = 5 
    result = num_k_len_substring_no_repeats(S, K)
    print(f'result -> {result}')
