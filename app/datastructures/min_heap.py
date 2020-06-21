class EmptyHeap(Exception):
    def __str__(self):
        return f'Exception: Empty heap'


class MinHeap:
    """Min heap implementation"""
    def __init__(self, items=None):
        self.items = items

    def _get_parent(self, child_idx):
        return child_idx // 2

    def _get_left_child(self, parent_idx):
        return 2 * parent_idx

    def _get_right_child(self, parent_idx):
        return 2 * parent_idx + 1

    def _has_left_child(self, idx):
        pass

    def _has_right_child(self, idx):
        pass

    def _has_parent(self, idx):
        pass

    def _sift_up(self):
        pass

    def _sift_down(self):
        pass

    def _min_heapify(self):
        pass

    def _swap(self, idx_one, idx_two):
        """Swaps the values at two indices"""
        self.items[idx_one], self[idx_two] = self[idx_two], self[idx_one]

    def peek(self):
        """Returns the minimum value in the heap"""
        if not self.items:
            raise EmptyHeap()

        return self.items[0]

    def add(self, val):
        pass

    def remove(self):
        pass


if __name__ == '__main__':
    items = [20, 13, 9, 10, 8, 3, 4, 15, 7]
    heap = MinHeap(items)
    heap.peek()
