from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def level_order_traversal(root):
    curr_queue = deque([])
    next_queue = deque([root])
    levels = []

    while next_queue:
        curr_queue = next_queue
        next_queue = deque([])
        level = []

        while curr_queue:
            node = curr_queue.pop()
            level.append(node.value)

            if node.left:
                next_queue.append(node.left)

            if node.right:
                next_queue.append(node.right)

        levels.append(level)
    return levels


if __name__ == '__main__':
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)

    one.left = two
    one.right = three

    two.left = four
    two.right = five

    three.left = six
    three.right = seven

    tree = one
    res = level_order_traversal(tree)
    print(f'res {res}')
