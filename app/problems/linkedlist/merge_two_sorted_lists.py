class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_sorted_list(nums):
    nums.sort()
    head = ListNode()
    node = head 

    for num in nums:
        node.next = ListNode(num)
        node = node.next

    return head.next



def merge_two_sorted_lists_iterative(p1, p2):
    dummy_node = ListNode()
    ans = dummy_node

    while p1 and p2:
        if p1.val < p2.val:
            ans.next = p1
            p1 = p1.next
        else:
            ans.next = p2
            p2 = p2.next
        ans = ans.next

    if p1:
        ans.next = p1

    if p2:
        ans.next = p2

    return dummy_node.next


def merge_two_sorted_lists_recursive(p1, p2):
    if p1 is None:
        return p2
    elif p2 is None:
        return p1
    elif p1.val < p2.val:
        p1.next = merge_two_sorted_lists_recursive(p1.next, p2)
        return p1
    else:
        p2.next = merge_two_sorted_lists_recursive(p1, p2.next)
        return p2


if __name__ == '__main__':
    nums_1 = [1, 4, 5]
    nums_2 = [2,3,7,9,11]

    p1 = create_sorted_list(nums_1)
    p2 = create_sorted_list(nums_2)

    merged_head = merge_two_sorted_lists(p1, p2)
    node = merged_head

    while node:
        print(node.val)
        node = node.next

    print('finished')

    
    
