from collections import deque, Counter


def use_deque():
    q = deque([1])
    value = q.pop()
    print(f'value {value}')
    q.appendleft(2)
    q.appendleft(3)
    q.appendleft(4)
    value = q.pop()
    print(f'value {value}')
    print(q)


def rotate_deque():
    q = deque([1, 2, 3])
    q.rotate(1) # deque([3, 1, 2])
    q.rotate(-1) # deque([1, 2, 3])

def maxlen_deque():
    q = deque([1, 2, 3], maxlen=2) # deque([2, 3])
    q.appendleft(7) # deque([7, 2])
    q.append(10) # deque([2, 10])

def counters():
    cnter = Counter('abcddaaa')
    cnter.update({'a': 1}) # increment 'a' count by 1
    cnter.update({'a': -1}) # decrement 'a' count by 1
    print(cnter.most_common()) # [('a', 4), ('d', 2), ('b', 1), ('c', 1)]
    print(cnter.most_common(1) # [('a', 4)]

    cnter_2 = Counter('abc'))
    diff = cnter_2 - cnter # Counter() empty len 0
    assert len(diff) == 0

    cnter.pop('a') # 4, Counter({'b': 1, 'c': 1, 'd': 2})
    cnter.popitem() # ('d', 2)
    cnter.popitem() # ('c', 1)





if __name__ == '__main__':
    use_deque()
