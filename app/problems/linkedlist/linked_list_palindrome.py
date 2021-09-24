class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_linked_list(head):
    p1, p2 = head, head.next
    p1.next = None

    while p2:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3

    return p1


def linked_list_palindrome(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second_half = reverse_linked_list(slow)
    first_half = head

    while second_half:
        if first_half.value != second_half.value:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True


if __name__ == '__main__':
    one = LinkedList('a')
    two = LinkedList('b')
    three = LinkedList('c')
    four = LinkedList('b')
    five = LinkedList('a')

    one.next = two
    two.next = three
    three.next = four
    four.next = five

    head = one
    res = linked_list_palindrome(head)
    print(f'res {res}')


    # node = res
    # while node:
    #     print(f'node {node.value}')
    #     node = node.next 
