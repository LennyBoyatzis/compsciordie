from collections import deque

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None


def build_graph(tree, target):
    target_node = None

    def dfs(node):
        nonlocal target_node
        if node:
            parent = node
            if node.value == target:
                target_node = node
                
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left:
                left.parent = parent
            if right:
                right.parent = parent

            return node

    dfs(tree)
    return target_node


def find_nodes_distance_k(tree, target, k):
    target_ref = build_graph(tree, target)

    queue = deque([(target_ref, 0)])
    nodes = []
    visited = set()

    while queue:
        node, depth = queue.pop()
        visited.add(node.value)

        if depth == k:
            nodes.append(node.value)

        neighbours = [node.left, node.right, node.parent]

        for neighbour in neighbours:
            if neighbour and neighbour.value not in visited:
                queue.appendleft((neighbour, depth + 1))
    return nodes


if __name__ == '__main__':
    one = BinaryTree(1)
    two = BinaryTree(2)
    three = BinaryTree(3)
    four = BinaryTree(4)
    five = BinaryTree(5)
    six = BinaryTree(6)
    seven = BinaryTree(7)
    eight = BinaryTree(8)

    one.left = two
    one.right = three

    two.left = four
    two.right = five

    three.right = six
    six.left = seven
    six.right = eight

    tree = one
    target = 3 
    k = 2 

    ans = find_nodes_distance_k(tree, target, k)

    print(f'ans {ans}')
