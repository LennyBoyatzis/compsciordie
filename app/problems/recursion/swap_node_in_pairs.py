class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swap_pairs(head):
    # If the list has no node or has only one node left.
    if not head or not head.next:
        return head

    # Nodes to be swapped
    first_node = head
    second_node = head.next
    third_node = second_node.next

    # Swapping
    first_node.next = swap_pairs(third_node)
    second_node.next = first_node

    # Now the head is the second node
    return second_node


if __name__ == '__main__':
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)

    one.next = two
    two.next = three
    three.next = four

    head = swap_pairs(one)
    node = head

    while node:
        print(node.val)
        node = node.next
