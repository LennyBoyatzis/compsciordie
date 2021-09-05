from collections import Counter


def min_chars_for_words(words):
    max_counts = Counter()

    for word in words:
        word_counts = Counter(word)

        for char, count in word_counts.items():
            if char in max_counts:
                max_counts[char] = max(max_counts[char], count)
            else:
                max_counts[char] = count

    ans = []

    for char, count in max_counts.items():
        ans.extend([char]*count)

    return ans


if __name__ == '__main__':
    words = ['this', 'that', 'did', 'deed', 'them!', 'a']
    res = min_chars_for_words(words)
    print(f'res {res}')
