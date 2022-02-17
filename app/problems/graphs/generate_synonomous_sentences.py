from collections import defaultdict, deque


def generate_sentences(synonyms, text):
    graph = defaultdict(set)
    queue = deque()
    ans = set()
    queue.append(text)

    for a, b in synonyms:
        graph[a].add(b)
        graph[b].add(a)

    while queue:
        sentence = queue.pop()
        ans.add(sentence)
        words = sentence.split()

        for i, word in enumerate(words):
            if word in graph:
                for synonym in graph[word]:
                    new_sentence = ' '.join(words[:i]+[synonym]+words[i+1:])
                    if new_sentence not in ans:
                        queue.appendleft(new_sentence)

    return sorted(list(ans))


if __name__ == '__main__':
    synonyms = [
        ['happy', 'joy'],
        ['sad', 'sorrow'],
        ['joy','cheerful']
    ]

    text = 'I am happy today but was sad yesterday'

    res = generate_sentences(synonyms, text)
    print(f'res {res}')
