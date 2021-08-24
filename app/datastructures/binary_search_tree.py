from typing import List


class BST:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value: int):
        if value < self.value:
            if not self.left:
                self.left = BST(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BST(value)
            else:
                self.right.insert(value)

        return self

    def contains(self, value: int):
        if value < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(value)
        else:
            return True

    def remove(self, value: int):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self

if __name__ == '__main__':
    tree = BST(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(2)
    tree.insert(5)
    tree.insert(1)

    contains_1 = tree.contains(1)
    print(f'contains_1 {contains_1}')

