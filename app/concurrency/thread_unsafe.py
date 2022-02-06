from threading import Thread

"""
Warning:
    Difference behaviour observed between python3.7 and 3.10
    The difference is explained here

    https://stackoverflow.com/questions/69993959/python-threads-difference-for-3-10-and-others
"""

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        for _ in range(100000):
            self.count += 1


num_threads = 5
threads = [0] * num_threads
counter = Counter()

for i in range(num_threads):
    threads[i] = Thread(target=counter.increment)

for i in range(num_threads):
    threads[i].start()

for i in range(num_threads):
    threads[i].join()

print(f'counter.count {counter.count}')
