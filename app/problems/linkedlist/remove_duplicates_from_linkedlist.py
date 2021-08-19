# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_duplicates_from_linked_list(linked_list: LinkedList) -> LinkedList:
    """Dedups a sorted linked list"""
	curr_node = linked_list
	
	while curr_node:
		next_distinct_node = curr_node.next

		while next_distinct_node and next_distinct_node.value == curr_node.value:
			next_distinct_node = next_distinct_node.next
		
		curr_node.next = next_distinct_node
		curr_node = next_distinct_node
		
    return linked_list
