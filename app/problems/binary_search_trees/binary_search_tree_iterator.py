class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Iterative Approach with Stack -> Worst Space O(n), Best Space O(log(n))
class BSTIterator:
    def __init__(self, root):
        self.node = root
        self.stack = [(root, False)]

    def next(self):
        if not self.stack:
            return

        while self.stack:
            node, visited = self.stack.pop()

            if visited:
                return node.value
            else:
                if node.right:
                    self.stack.append((node.right, False))

                self.stack.append((node, True))

                if node.left:
                    self.stack.append((node.left, False))

    def hasNext(self):
        return len(self.stack) > 0


def iterative_inorder_traversal(root):
    path, stack = [], [(root, False)]

    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                path.append(node.value)
            else: # preorder: left -> root -> right
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
    return path


if __name__ == '__main__':
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)
    nine = TreeNode(9)

    one.left = two
    one.right = three
    two.left = four
    three.left = six
    three.right = seven
    four.right = nine

    #         1
    #        / \
    #       2   3
    #      /   / \
    #     4    6  7
    #      \
    #       9

    # 4, 9, 2, 1, 6, 3, 7

    res = iterative_inorder_traversal(one)
    print(f'res: {res}') # 4, 9, 2, 1, 6, 3, 7

    it = BSTIterator(one)

    print(it.next()) # 4
    print(it.next()) # 9
    print(it.next()) # 2
    print(it.next()) # 1
    print(it.next()) # 6
    print(it.next()) # 3
    print(it.next()) # 7

