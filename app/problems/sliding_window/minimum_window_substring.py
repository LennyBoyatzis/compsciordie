from collections import Counter


"""
How can we know if a string contains all the chars?

{
    'A': 2,
    'D': 2,
    'O': 2,
    'B': 2,
    'E': 2,
    'C': 2,
    'N': 1
}

{
    'A': 2
    'C': 2,
    'B': 2
}
"""


def min_window_substring(S, T):
    """
    No Window: Return ''

    1. Start with two pointers, left and right, initially pointing to the first
    element of S

    2. Use right pointer to expand window until we get a desirable window
    (which contains all characters of T)

    3. Once we have a window with all the chars, we can move ahead by one. If
    the window is still desirable we keep updating the window size

    4. If the window is not desireable, we REPEAT step 2
    """
    left, right = 0, 0
    s_counter = Counter(S)
    t_counter = Counter(T)

    while right <= len(S) - 1:
        char = S[right]
    #     char_freq[char] += 1
    #     right += 1

    # print(f'chars {char_freq}')



if __name__ == '__main__':
    S = 'ADOBECODEBANC'
    T = 'ABC'
    result = min_window_substring(S, T)
    print(f'result {result}')
