from app.datastructures.double_linked_list import DoubleLinkedList


class DoubleEndedQueue(DoubleLinkedList):
    def __init__(self, nums):
        self.build_from_list(nums)

    def append(self, val):
        self.append(val)

    def pop(self):
        self.popback()

    def popleft(self):
        self.popfront()

    def appendleft(self, val):
        self.prepend(val)


if __name__ == '__main__':
    deque = DoubleEndedQueue([1, 2, 3, 4, 5])
    deque.appendleft(10)
    deque.appendleft(9)
    deque.appendleft(8)
    deque.appendleft(7)
    deque.pop()
    deque.popleft()
    node = deque.head

    while node:
        print(f'node.val {node.val}')
        node = node.next
