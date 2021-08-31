class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


if __name__ == '__main__':
    root = Node('A')
    root.children.append([Node('B'), Node('C'), Node('D')])
    root.left
