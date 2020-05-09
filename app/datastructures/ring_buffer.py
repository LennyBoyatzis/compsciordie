"""
- RingBuffer/Cirular Buffer/Circular Lists
- FIFO queue of fixed size
"""


class RingBuffer:
    """Queue which overrides the oldest element when full"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.write_index = 0

    def is_full(self):
        """Checks if buffer is at capacity"""
        return self.write_index == self.capacity

    def reset(self):
        """Resets write index to 0"""
        self.write_index = 0

    def append(self, val):
        """Appends val to ring buffer"""
        if self.is_full():
            self.reset()

        self.queue[self.write_index] = val
        self.write_index += 1

    def get(self):
        """Returns list of elements in queue"""
        return self.queue


if __name__ == '__main__':
    buf = RingBuffer(5)
    buf.append(10)
    buf.append(20)
    buf.append(30)
    buf.append(40)
    buf.append(50)
    buf.append(60)
    buf.append(70)

    queue = buf.get()
    print(f'queue {queue}')  # [60, 70, 30, 40, 50]
