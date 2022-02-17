def build_trie(words):
    trie = {}
    node = trie

    for word in words:
        node = trie

        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        
        if '*' in node:
            node['*'].append(word)
        else:
            node['*'] = [word]

    return trie


def search(trie, word):
    node = trie

    for char in word:
        if char not in node:
            return False
        node = node[char]

    if '*' in node:
        return word in node['*']

    return False



if __name__ == '__main__':
    words = ['cat', 'car', 'dog', 'pickle', 'pick']
    trie = build_trie(words)
    print(f'trie {trie}')

    contains_node = search(trie, 'do')
    print(f'contains_node {contains_node}')
