def length_of_longest_substring_naive(s: str) -> int:
    """Returns the length of the longest substring without repeating chars"""
    if not s:
        return 0

    size = len(s)
    max_len = 1 

    for i in range(size):
        for j in range(i+1, size):
            substring = s[i:j+1]
            substring_len = len(substring)
            unique_chars = set(substring)
            if substring_len == len(unique_chars):
                max_len = max(max_len, substring_len)
    return max_len

def length_of_longest_substring(s: str) -> int:
    """
    Time:  O(n)
    Space: O(k)
    [k = length of the longest substring w/o repeating characters]
    """
    longest = 0
    left, right = 0, 0
    size = len(s)
    chars = set()
    while left < size and right < size: 
        if s[right] not in chars:
            chars.add(s[right])
            right += 1
            longest = max(longest, right - left)
        else:
            chars.remove(s[left])
            left += 1
    return longest


if __name__ == '__main__':
    text = 'pwwkew'
    result = length_of_longest_substring(text)
    print(f'result {result}')
    assert result == 3

    text_2 = 'bbbbb'
    result_2 = length_of_longest_substring(text_2)
    print(f'result_2 {result_2}')
    assert result_2 == 1 

    text_3 = 'abcabcbb'
    result_3 = length_of_longest_substring(text_3)
    print(f'result_3 {result_3}')
    assert result_3 == 3 
