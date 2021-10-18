class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#       4
#      /  \
#     1    5
#         /  \
#        3    2

# in-order, pre-order, post-order
def in_order_traversal(tree):
    leaves = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)
        
        if not node.left and not node.right:
            leaves.append(node.value)

        dfs(node.right)

    dfs(tree)
    return leaves


def leave_match(l1, l2):
    if len(l1) != len(l2):
        return False

    size = len(l1)

    for i in range(size):
        if l1[i] != l2[i]:
            return False
    return True


def compare_leaf_traversal(tree1, tree2):
    tree_1_leaves = in_order_traversal(tree1)
    tree_2_leaves = in_order_traversal(tree2)

    print(tree_1_leaves)
    print(tree_2_leaves)

    return leave_match(tree_1_leaves, tree_2_leaves)


if __name__ == '__main__':
    alpha_1 = BinaryTree(1)
    alpha_2 = BinaryTree(2)
    alpha_3 = BinaryTree(3)
    alpha_4 = BinaryTree(4)
    alpha_5 = BinaryTree(5)
    alpha_6 = BinaryTree(6)
    alpha_7 = BinaryTree(7)
    alpha_8 = BinaryTree(8)

    alpha_1.left = alpha_2
    alpha_1.right = alpha_3

    alpha_2.left = alpha_4
    alpha_2.right = alpha_5

    alpha_3.right = alpha_6

    alpha_5.left = alpha_7
    alpha_5.right = alpha_8

    tree1 = alpha_1
    
    beta_1 = BinaryTree(1)
    beta_2 = BinaryTree(2)
    beta_3 = BinaryTree(3)
    beta_4 = BinaryTree(4)
    beta_5 = BinaryTree(5)
    beta_6 = BinaryTree(6)
    beta_7 = BinaryTree(7)
    beta_8 = BinaryTree(8)

    beta_1.left = beta_2
    beta_1.right = beta_3

    beta_2.left = beta_4
    beta_2.right = beta_7

    beta_3.right = beta_5

    beta_5.left = beta_8
    beta_5.right = beta_6

    tree2 = beta_1

    res = compare_leaf_traversal(tree1, tree2)
    print(f'res {res}')
