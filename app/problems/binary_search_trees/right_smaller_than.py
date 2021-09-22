class BST:
    def __init__(self, value):
        self.value = value
        self.left_subtree_size = 0
        self.left = None
        self.right = None

    def insert(self, value, idx, ans, num_smaller_at_ins=0):
        if value < self.value:
            # Value goes to the LHS
            self.left_subtree_size += 1
            if self.left is None:
                self.left = BST(value)
                ans[idx] = num_smaller_at_ins
            else:
                self.left.insert(value, idx, ans, num_smaller_at_ins)
        else:
            # Value goes to the RHS
            num_smaller_at_ins += self.left_subtree_size
            if value > self.value:
                num_smaller_at_ins += 1

            if self.right is None:
                self.right = BST(value)
                ans[idx] = num_smaller_at_ins
            else:
                self.right.insert(value, idx, ans, num_smaller_at_ins)
        return self


def right_smaller_than(array):
    if len(array) == 0:
        return []

    size = len(array)
    bst = BST(array[-1])
    ans = [0] * size

    for i in range(size-2, -1, -1):
        bst.insert(array[i], i, ans)

    return ans


if __name__ == '__main__':
    array = [8, 5, 11, -1, 3, 4, 2]
    expected = [5, 4, 4, 0, 1, 1, 0]
    ans = right_smaller_than(array)
    print(f'ans {ans}')
