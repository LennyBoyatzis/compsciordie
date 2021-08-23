def decompress_string(text: str) -> str:
    """Decompresses string"""
    stack = []
    ans, chars, digits = '', '', ''

    for char in text:
        if char.isdigit():
            digits += char 

        if char.isalpha():
            chars += char

        if char == '[':
            if chars and stack:
                stack[-1][1] += chars
                chars = ''
            elif chars and not stack:
                stack.append(['1', chars])
                chars = ''

            digits = digits if digits else '1'
            stack.append([digits, ''])
            digits = ''
        elif char == ']':
            stack[-1][1] += chars
            digit, text = stack.pop()

            if stack:
                stack[-1][1] += int(digit) * text
            else:
                ans += int(digit) * text
            chars = ''

    if stack:
        digit, text = stack.pop()
        ans += int(digit) * text

    if chars:
        ans += chars

    return ans


if __name__ == '__main__':
    test_one_input = '3[a]2[bc]'
    test_one_expected = 'azazbb'
    print(f'one: {decompress_string(test_one_input)}')

    test_two_input = '2[3[a]c]'
    test_two_expected = 'aaac' * 2
    print(f'two: {decompress_string(test_two_input)}')

    test_three_input = 'a[]b'
    test_three_expected = 'ab'
    print(f'three: {decompress_string(test_three_input)}')

    test_four_input = '0[abc]'
    test_four_expected = ''
    print(f'four: {decompress_string(test_four_input)}')

    test_five_input = 'abc3[cd]xyz'
    test_five_expected = ''
    print(f'five: {decompress_string(test_five_input)}')

