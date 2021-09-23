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


def inorder_traversal(bst, target_val):
    """Perform inorder traversal to find inorder successor"""
    successor = None
    previous_val = None

    def recurse(node):
        nonlocal successor
        nonlocal previous_val

        if not node:
            return

        recurse(node.left)

        if previous_val == target_val:
            successor = node.value
            return

        previous_val = node.value

        recurse(node.right)

    recurse(bst)
    return successor


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
    target_node = find_target_node(bst, target_val)

    if target_node.right:
        # Case 1: Simply find the leftmost node in the subtree rooted at target_node.right
        leftmost = target_node.right
        while leftmost.left:
            leftmost = leftmost.left

        return leftmost
    else:
        # Case 2: Perform inorder traversal and keep track of previous node
        return inorder_traversal(bst, target_node.value)


if __name__ == '__main__':
    array = [7, 4, 10, 2, 8, 12, 3] 
    bst = TreeNode(array[0])

    for i in range(1, len(array)):
        bst.insert(array[i])

    target_val = 4 
    successor = find_inorder_successor(bst, target_val)
    print(f'successor {successor}')
