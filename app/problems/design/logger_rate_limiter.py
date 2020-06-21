import heapq


class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = set()
        self.heap = []

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp,
        otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        threshold = timestamp - 10

        while self.heap and self.heap[0][0] <= threshold:
            (ts, msg) = heapq.heappop(self.heap)
            self.vals.remove(msg)

        if message in self.vals:
            return False

        heapq.heappush(self.heap, (timestamp, message))
        self.vals.add(message)

        return True


if __name__ == '__main__':
    logger = Logger()
    logger.shouldPrintMessage(1, "foo")
    logger.shouldPrintMessage(2, "bar")
    logger.shouldPrintMessage(3, "foo")
    logger.shouldPrintMessage(11, "foo")
