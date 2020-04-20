import heapq
from app.datastructures.single_linked_list import SingleLinkedList


class WrapperNode:
    def __init__(self, node):
        self.node = node
        self.val = node.val
        self.next = node.next

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val


def merge_k_sorted_lists(lists):
    merged_list = []
    heap = []

    for node in lists:
        heapq.heappush(heap, node)

    while heap:
        top = heapq.heappop(heap)
        merged_list.append(top.val)
        top = top.next

        if top:
            heapq.heappush(heap, WrapperNode(top))

    return SingleLinkedList(merged_list)


if __name__ == '__main__':
    l1 = SingleLinkedList([1, 4, 5])
    l2 = SingleLinkedList([1, 3, 4])
    l3 = SingleLinkedList([2, 6])
    merged_list = merge_k_sorted_lists([l1.head, l2.head, l3.head])
    node = merged_list.head

    while node:
        print(f'node {node}')
        node = node.next
