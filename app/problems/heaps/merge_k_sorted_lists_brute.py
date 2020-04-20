from app.datastructures.single_linked_list import SingleLinkedList


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_k_sorted_lists(lists):
    """
    k = Number of linked lists
    N = Number of nodes in output linked list

    Space:
        - O(N)
            - Need N nodes to store the final linked list
    Time:
        - O(N log N)
            - Sort through a list of length N
    """
    nodes = []

    for node in lists:
        while node:
            nodes.append(node)
            node = node.next

    nodes_sorted = sorted(nodes, key=lambda node: node.val)

    dummy = ListNode(0)
    pointer = dummy

    for node in nodes_sorted[1:]:
        pointer.next = node
        pointer = pointer.next

    return dummy.next


if __name__ == '__main__':
    l1 = SingleLinkedList([1, 4, 5])
    l2 = SingleLinkedList([1, 3, 4])
    l3 = SingleLinkedList([2, 6])
    head = merge_k_sorted_lists([l1.head, l2.head, l3.head])

    node = head

    while node:
        print(f'node {node.val}')
        node = node.next
