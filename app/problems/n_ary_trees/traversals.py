from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


def bfs_levelorder_traversal(root):
    queue = deque([root])
    path = []

    while queue:
        node = queue.pop()
        path.append(node.value)

        for node in node.children:
            queue.appendleft(node)

    return path


def bfs_levelorder_traversal_tiered(root):
    if not root:
        return []

    curr_queue, next_queue = None, deque([root])
    levels = []

    while next_queue:
        curr_queue = next_queue
        next_queue = deque([])
        level = []

        while curr_queue:
            node = curr_queue.pop()
            if node:
                level.append(node.value)

                for child in node.children:
                    next_queue.appendleft(child)
        levels.append(level)
    return levels


# Visit root node first, then children nodes
def dfs_preorder_traversal(root):
    path = []

    def recurse(node):
        if not node:
            return

        path.append(node.value)

        for node in node.children:
            recurse(node)


    recurse(root)
    return path


# Visit children nodes before the root
def dfs_postorder_traversal(root):
    path = []

    def recurse(node):
        for child in node.children:
            recurse(child)
        path.append(node.value)

    recurse(root)
    return path


# Visit children nodes before the root
def dfs_postorder_traversal_iterative(root):
    stack = [root]
    path = []

    while stack:
        node = stack.pop()
        path.append(node.value)
        stack.extend(node.children)

    return path[::-1]


if __name__ == '__main__':
    a = TreeNode('A')
    b = TreeNode('B')
    c = TreeNode('C')
    d = TreeNode('D')
    e = TreeNode('E')
    f = TreeNode('F')
    g = TreeNode('G')

    a.children.extend([b, c, d])
    c.children.extend([e, f])
    d.children.extend([g])

    root = a

    pre_order = dfs_preorder_traversal(root) 
    print(f'pre_order {pre_order}') #A->B->C->E->F->D->G.  

    post_order = dfs_postorder_traversal(root)
    print(f'post_order {post_order}') # B->E->F->C->G->D->A.

    post_order_iterative = dfs_postorder_traversal_iterative(root)
    print(f'post_order_iterative {post_order_iterative}') # B->E->F->C->G->D->A.

    level_order = bfs_levelorder_traversal(root)
    print(f'level_order {level_order}') # A->B->C->D->E->F->G. 

    level_order_tiered = bfs_levelorder_traversal_tiered(root)
    print(f'level_order_tiered {level_order_tiered}') # [A]->[B->C->D]->[E->F->G]. 
