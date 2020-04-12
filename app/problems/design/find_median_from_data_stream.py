import bisect


class MedianFinder:
    def __init__(self):
        self.store = []

    def addNum(self, num):
        bisect.insort(self.store, num)

    def findMedian(self):
        size = len(self.store)
        mid = size // 2
        if size % 2 == 0:
            return (self.store[mid-1] + self.store[mid]) / 2
        else:
            return self.store[mid]
