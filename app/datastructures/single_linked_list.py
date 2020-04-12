class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SingleLinkedList:
    def __init__(self, nums):
        self.head = Node(nums[0])
        node = self.head
        self.build_from_list(node, nums[1:])

    def build_from_list(self, node, nums):
        """Builds linked list from array"""
        for val in nums:
            node.next = Node(val)
            node = node.next

    def append(self, val):
        """Adds node to back of list"""
        node = self.head

        while node.next:
            node = node.next

        new_node = Node(val)
        node.next = new_node

    def prepend(self, val):
        """Adds node to front of list"""
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insert(self, predecessor, val):
        """Inserts node into the list after a given node"""
        node = self.head

        while node.next:
            if node is predecessor:
                tmp = node.next
                new_node = Node(val)
                node.next = new_node
                new_node.next = tmp
                break
            node = node.next

    def popfront(self):
        """Remove node from front of list and return val"""
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None

    def popback(self):
        """Remove node from back of list and return val"""
        if not self.head or not self.head.next:
            self.head = None
        else:
            p1, p2 = self.head, self.head.next

            while p2.next:
                p1 = p2
                p2 = p2.next

            p1.next = None


if __name__ == '__main__':
    linked_list = SingleLinkedList([1, 2, 3, 4, 5])
    linked_list.append(20)
    linked_list.prepend(100)
    node = linked_list.head
    linked_list.insert(node, 44)
    linked_list.popback()

    while node:
        print(f'node.val {node.val}')
        node = node.next
