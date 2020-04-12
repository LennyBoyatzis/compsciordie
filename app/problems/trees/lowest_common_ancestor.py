class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    ans = []

    def dfs(root):
        if not root:
            return False

        left = dfs(root.left)
        right = dfs(root.right)

        p_or_q = root.val == p or root.val == q

        if (p_or_q or left) and (p_or_q or right):
            ans.append(root.val)

        return left or right or p_or_q

    dfs(root)
    return ans[-1]


if __name__ == '__main__':
    root = TreeNode(3)
    one = TreeNode(5)
    two = TreeNode(1)
    three = TreeNode(6)
    four = TreeNode(2)
    five = TreeNode(0)
    six = TreeNode(8)
    seven = TreeNode(7)
    eight = TreeNode(4)

    root.left = one
    root.right = two

    one.left = three
    one.right = four

    two.left = five
    two.right = six

    four.left = seven
    four.right = eight

    result = lowest_common_ancestor(root, 6, 0)
    print(f'result {result}')
