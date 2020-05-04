from collections import Counter


def expressive_words(S, words):
    S_counter = Counter(S)
    res = 0

    for word in words:
        word_counter = Counter(word)
        count = 0
        for char, count in word_counter.items():
            if char in S_counter:
                if S_counter[char] >= count and S_counter[char] >= 3:
                    count += 1

        if count == len(word_counter):
            res += 1

    return res


if __name__ == '__main__':
    S = 'heeellooo'
    words = ['hello', 'hi', 'helo']
    result = expressive_words(S, words)
    print(f'result {result}')
