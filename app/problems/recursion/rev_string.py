def reverse_string(text, left, right):
    if left < right:
        text[left], text[right] = text[right], text[left]
        reverse_string(text, left+1, right-1)

    return ''.join(text)


if __name__ ==  '__main__':
    text = list('batter')
    left, right = 0, len(text) - 1
    result = reverse_string(text, left, right)
    print(f'result {result}')
