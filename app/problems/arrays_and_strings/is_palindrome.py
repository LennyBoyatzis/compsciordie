def is_palindrome(string: str) -> bool:
    """Checks if string is a palindrome"""
    left, right = 0, len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True

def find_longest_pal_from_center(left, right, string):
    while left >= 0 and right <= len(string) - 1:
        if string[left] == string[right]:
            left -= 1
            right += 1
        else:
            break

    return string[left+1:right]

def longest_palindromic_substring(string):
    max_substring = string[0]

    for i in range(1, len(string)):
        substring_odd = find_longest_pal_from_center(i, i, string)
        substring_even = find_longest_pal_from_center(i-1, i, string)
        max_substring = max(substring_odd, substring_even, max_substring, key=len)
    return max_substring


if __name__ == '__main__':
    string = 'xyzazyx'
    res = is_palindrome(string)
    print(res)

    string = 'abaxyzazyxf'
    res = longest_palindromic_substring(string)
    print(f'res: {res}')

    string = 'abaxyzzyxf'
    string = 'kxyzaazyxf'
    res = find_longest_pal_from_center(4, 5, string)
    print(f'res: {res}')
