from typing import List
from collections import defaultdict


def equivalent_dominoes(dominoes: List[List[int]]) -> int:
    """Counts number of domino pairs in a list"""
    d, ans = defaultdict(int), 0

    for a, b in dominoes:
        key = min(a, b), max(b, a)
        print(f'what is the key {key}')
        ans += d[key]
        d[key] += 1

    return ans


if __name__ == '__main__':
    dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 3]]
    expected = 3
    result = equivalent_dominoes(dominoes)
    print(f'result {result}')
    assert result == expected
