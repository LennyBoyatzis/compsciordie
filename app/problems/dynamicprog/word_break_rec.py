def word_break(text, word_dict):
    """
    Returns bool if text composed of word_dict words
    """
    def search(text, word_dict, start):
        if start == len(text):
            return True

        for i in range(start, len(text)):
            if text[start:i+1] in word_dict:
                if search(text, word_dict, i+1):
                    return True
        return False

    return search(text, set(word_dict), 0)


if __name__ == '__main__':
    text = 'leetcode'
    word_dict = ['leet', 'code']
    result = word_break(text, word_dict)
    assert result is True

    text_2 = 'applepenapple'
    word_dict_2 = ['apple', 'pen']
    result_2 = word_break(text_2, word_dict_2)
    assert result_2 is True

    text_3 = 'catsandog'
    word_dict_3 = ['cats', 'dog', 'sand', 'and', 'cat']
    result_3 = word_break(text_3, word_dict_3)
    assert result_3 is False
