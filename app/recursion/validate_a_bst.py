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


def validate_bst(node, low, high):
    if not node:
        return True

    if not low < node.value <= high:
        return False

    left = validate_bst(node.left, low, node.value)
    right = validate_bst(node.right, node.value, high)

    return left and right

if __name__ == '__main__':
    array = [7, 4, 10, 2, 8, 12, 3] 
    bst = TreeNode(array[0])

    for i in range(1, len(array)):
        bst.insert(array[i])

    is_valid = validate_bst(bst, float('-inf'), float('inf'))
    print(f'is_valid {is_valid}')
