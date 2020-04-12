class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self, nums):
        self.head = None
        self.tail = None
        self.build_from_list(nums)

    def build_from_list(self, nums):
        self.head = Node(nums[0])
        node = self.head

        for val in nums[1:]:
            node.next = Node(val)
            node.next.prev = node
            node = node.next

        self.tail = node

    def append(self, val):
        node = self.tail
        node.next = Node(val)
        self.tail = node.next
        self.tail.prev = node

    def prepend(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def popfront(self):
        if not self.head or not self.head.next:
            self.head = None
        else:
            self.head = self.head.next

    def popback(self):
        new_tail = self.tail.prev
        new_tail.next = None
        self.tail = new_tail


if __name__ == '__main__':
    linked_list = DoubleLinkedList([1, 2, 3, 4, 5])
    linked_list.prepend(20)
    linked_list.append(99)
    linked_list.append(102)
    linked_list.prepend(-34)
    linked_list.prepend(12)
    linked_list.popfront()
    linked_list.popback()
    node = linked_list.head

    while node:
        print(f'node.val {node.val}')
        node = node.next
