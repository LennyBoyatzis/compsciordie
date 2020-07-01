import heapq


class Sentence:
    def __init__(self, text, search_count):
        self.text = text
        self.search_count = search_count

    def __lt__(self, other_text):
        pass

    def __eq__(self, other_text):
        pass


class TrieNode:
    def __init__(self, key):
        self.key = key
        self.children = {}
        self.valid_sentences = []

    def __str__(self):
        return f'key: {self.key}, children: {self.children}, valid_sentences: {self.valid_sentences}'


class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.store = TrieNode('*')
        self.curr_node = self.store

        for (text, times) in zip(sentences, times):
            node = self.store
            for c in text:
                if c not in node.children:
                    node.children[c] = TrieNode(c)

                node.valid_sentences.append(text)
                node = node.children[c]

            node.children['#'] = True
            node.valid_sentences.append((text, times))

    def input(self, c):
        curr_node = self.curr_node

        if c is '#':
            return curr_node.valid_sentences
        elif c in curr_node.children:
            curr_node = curr_node.children[c]
            return curr_node.valid_sentences
        else:
            curr_node.children[c] = TrieNode(c)
            curr_node = curr_node.children[c]

        return []


if __name__ == '__main__':
    times = [5, 3, 2, 2]
    sentences = [
        'i love you',
        'island',
        'iroman',
        'i love leetcode']

    searcher = AutocompleteSystem(sentences, times)

    print("i ", searcher.input("i"))
    print("  ", searcher.input(" "))
    print("a ", searcher.input("a"))
    print("# ", searcher.input("#"))
