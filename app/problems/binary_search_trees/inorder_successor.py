class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

    def insert(self, val):
        if self.value > val:
            if not self.left:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        else:
            if not self.right:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)


def find_target_node(bst, target_val):
    """Find node with target value"""
    node = bst

    while node:
        if node.value == target_val:
            return node
        elif node.value > target_val:
            node = node.left
        else:
            node = node.right
    return node


def find_inorder_successor(bst, target_val):
    """Find inorder successor for given target value"""
    node = bst
    successor = None

    while node:
        if target_val >= node.value:
            node = node.right
        else:
            successor = node
            node = node.left
    return successor.value if successor else successor


if __name__ == '__main__':
    array = [7, 4, 10, 2, 8, 12, 3] 
    bst = TreeNode(array[0])

    for i in range(1, len(array)):
        bst.insert(array[i])

    target_val = 4 
    successor = find_inorder_successor(bst, target_val)
    print(f'successor {successor}')
