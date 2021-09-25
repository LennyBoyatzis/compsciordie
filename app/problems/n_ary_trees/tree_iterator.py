import heapq
from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


class HeapNode:
    def __init__(self, node: TreeNode, cost: int):
        self.node = node
        self.cost = cost

    def __lt__(self, value):
        return self.cost < value

    def __gt__(self, value):
        return self.cost > value


class TreeIterator:
    def __init__(self, root: TreeNode):
        self.node = root
        self.pq = [HeapNode(root, root.value)]

    def get_next_leaf_node(self):
        if not self.pq:
            return None

        while self.pq:
            heap_node = heapq.heappop(self.pq)
            node, cost = heap_node.node, heap_node.cost

            if not node.children:
                return node.value

            for child in node.children:
                heapq.heappush(self.pq, HeapNode(child, cost+child.value))
        
    def __iter__(self):
        return self

    def __next__(self):
        return self.get_next_leaf_node()



if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(4)
    d = TreeNode(8)
    e = TreeNode(12)
    f = TreeNode(14)
    g = TreeNode(1)

    a.children.extend([b, c, d])
    c.children.extend([e, f])
    d.children.extend([g])

    #       1
    #    /  |  \
    #   2   4   8
    #      / \   \
    #     12 14   1

    # 2 -> 1 -> 12 -> 14

    root = a
    it = TreeIterator(root)

    print(next(it)) # -> 2
    print(next(it)) # -> 1
    print(next(it)) # -> 12
    print(next(it)) # -> 14
    print(next(it)) # -> None? 
