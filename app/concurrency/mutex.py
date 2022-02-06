from threading import Thread
from threading import Lock


class Counter:
    def __init__(self):
        self.count = 0
        self.lock = Lock()

    def increment(self):
        for _ in range(100000):
            self.lock.acquire()
            self.count += 1
            self.lock.release()


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
