class TreeNode:
    def __init__(self, val):
        self.value = val
        self.children = []


def get_lowest_common_manager(top, one, two):
    lowest_common = None

    def search(node):
        nonlocal lowest_common

        if not node:
            return 0

        child_sum = sum([search(child) for child in node.children])
        is_target = 1 if node.value == one.value or node.value == two.value else 0

        if not lowest_common and child_sum + is_target == 2:
            lowest_common = node

        return child_sum + is_target 

    search(top)
    return lowest_common



if __name__ == '__main__':
    a = TreeNode('A')
    b = TreeNode('B')
    c = TreeNode('C')
    d = TreeNode('D')
    e = TreeNode('E')
    f = TreeNode('F')
    g = TreeNode('G')
    h = TreeNode('H')
    i = TreeNode('I')

    a.children.extend([b, c])
    b.children.extend([d, e])
    c.children.extend([f, g])
    d.children.extend([h, i])

    res = get_lowest_common_manager(a, e, i)
    print(f'res -> {res.value}') # B
