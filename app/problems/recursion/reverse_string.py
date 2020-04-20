def reverse_string(s):
    def recurse(start, end):
        if start < end:
            s[start], s[end] = s[end], s[start]
            recurse(start+1, end-1)

    recurse(0, len(s) - 1)
    return s


if __name__ == '__main__':
    odd_string = ['h', 'e', 'l', 'l', 'o']
    assert reverse_string(odd_string) == ['o', 'l', 'l', 'e', 'h']

    even_string = ['w', 'o', 'r', 'd']
    assert reverse_string(even_string) == ['d', 'r', 'o', 'w']
