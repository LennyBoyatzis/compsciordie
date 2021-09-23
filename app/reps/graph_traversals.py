from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def level_order_traversal(node):
    queue = deque([node])
    path = []

    while queue:
        node = queue.pop()
        path.append(node.value)

        if node.left:
            queue.appendleft(node.left)
        if node.right:
            queue.appendleft(node.right)
    return path


def level_order_traversal_segmented(node):
    queue = deque([])
    next_queue = deque([node])
    levels = []

    while next_queue:
        queue = next_queue
        next_queue = deque([])
        level = []

        while queue:
            node = queue.pop()
            level.append(node.value)

            if node.left:
                next_queue.appendleft(node.left)

            if node.right:
                next_queue.appendleft(node.right)
        levels.append(level)
    return levels


def preorder_traversal(node):
    path = []

    def traverse(node):
        if not node:
            return

        path.append(node.value)
        traverse(node.left)
        traverse(node.right)

    traverse(node)
    return path


def inorder_traversal(node):
    path = []

    def traverse(node):
        if not node:
            return

        traverse(node.left)
        path.append(node.value)
        traverse(node.right)

    traverse(node)
    return path


def postorder_traversal(node):
    path = []

    def traverse(node):
        if not node:
            return

        traverse(node.left)
        traverse(node.right)
        path.append(node.value)
    
    traverse(node)
    return path


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

    res = level_order_traversal_segmented(tree)
    print(f'res {res}')

    res = preorder_traversal(tree)
    print(f'res {res}')

    res = inorder_traversal(tree)
    print(f'res {res}')

    res = postorder_traversal(tree)
    print(f'res {res}')
