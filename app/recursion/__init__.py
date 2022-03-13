from threading import Condition

# In python, a condition is a monitor (predicate combined with a mutex lock)
# Monitors enable threads to exercise mutual exclusion as well as cooperation

"""
     P1 P2 P3 
     \  |  / 
        *
        *
        *
        *
     /  |  \
    C1  C2 C3
"""


class BoundedBlockingQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.q = []
        self.cond = Condition()

    def enqueue(self, item):
        with self.cond:
            self.cond.wait_for(lambda: len(self.q) < self.capacity)
            self.q.append(item)
            self.cond.notify_all()

    def dequeue(self):
        with self.cond:
            self.cond.wait_for(lambda: len(self.q) > 0)
            item = self.q.pop(0)
            self.cond.notify_all()
            return item

    def size(self):
        return len(self.q)
