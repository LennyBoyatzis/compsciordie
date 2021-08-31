import string

WINDOW_CAP = 5


"""
window: abcde
window: bcdef
window: cdefg
window: defgh
window: efghi
window: fghij
window: ghijk
window: hijkl
"""

def rampup_sliding_window(letters):
    start, end = 0, 0 

    while end < len(letters):
        window_len = end - start
        if window_len == WINDOW_CAP:
            print(f'window: {letters[start:end]}')
            start += 1
        end += 1

"""
window: a
window: ab
window: abc
window: abcd
window: bcde
window: cde
window: de
window: e
window:
window: f
window: fg
window: fgh
window: fghi
window: ghij
window: hij
window: ij
window: j
"""

def pyramid_sliding_window(letters):
    start, end = 0, 0 

    while end < len(letters):
        window_len = end - start
        if window_len == WINDOW_CAP:
            while start < end:
                start += 1
                print(f'window: {letters[start:end]}')
        else:
            print(f'window: {letters[start:end]}')
        end += 1


if __name__ == '__main__':
    letters = string.ascii_lowercase
    pyramid_sliding_window(letters)
