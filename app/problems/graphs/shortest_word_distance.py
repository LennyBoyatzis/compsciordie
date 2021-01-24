from collections import defaultdict, Counter, deque


def build_graph(words):
    graph = defaultdict(list)
    size = len(words)

    for i in range(size-1):
        curr_word, next_word = words[i], words[i+1]
        graph[curr_word].append(next_word)

    for i in range(size-1, 0, -1):
        curr_word, next_word = words[i], words[i-1]
        graph[curr_word].append(next_word)

    return graph


def shortest_distance(words, word1, word2):
    counter = Counter(words)
    graph = build_graph(words)
    queue = deque([[word1, word2, 0], [word2, word1, 0]])
    smallest_dist = float('inf')

    while queue:
        node = queue.pop()
        word, target, distance = node

        print(f'word {word}')
        print(f'target {target}')

        if word == target:
            smallest_dist = min(distance, smallest_dist)

        counter[word] -= 1
        neighbours = graph[word]

        for neighbour in neighbours:
            if counter[neighbour] >= 0:
                queue.appendleft([neighbour, target, distance+1])

    return smallest_dist


if __name__ == '__main__':
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1, word2 = 'makes', 'coding'
    result = shortest_distance(words, word1, word2)
    print(f'result {result}')
