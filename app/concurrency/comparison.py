from threading import Thread
from multiprocessing import Process

from multiprocessing.managers import BaseManager
from queue import Queue
import time
import multiprocessing


class SumRange:
    def __init__(self):
        self.counter = 0

    def add_integers(self, start, end):
        for i in range(start, end + 1):
            self.counter += i

    def get_counter(self):
        return self.counter


def single_thread():
    obj = SumRange()
    start = time.time()
    obj.add_integers(1, 30000000)
    end = time.time() - start
    print(f'single thread took: {end} seconds and summed to {obj.counter}')


def multi_thread():
    obj1 = SumRange()
    obj2 = SumRange()

    start = time.time()

    t1 = Thread(target=obj1.add_integers, args=(1, 15000000))
    t2 = Thread(target=obj2.add_integers, args=(15000001, 30000000))

    t1.start()
    t2.start()


    t1.join()
    t2.join()

    combined_sum = obj1.counter + obj2.counter
    end = time.time() - start
    print(f'multi thread took: {end} seconds and summed to {combined_sum}')


def single_process(obj1, start, end):
    obj1.add_integers(start, end)


def multi_process():
    BaseManager.register('SumRange', SumRange)
    manager = BaseManager(address=('127.0.0.1', 63333))
    manager.start()


    obj1 = manager.SumRange()
    obj2 = manager.SumRange()

    start = time.time()

    p1 = Process(target=single_process, args=(obj1, 1, 15000000,))
    p2 = Process(target=single_process, args=(obj2, 15000001, 30000000,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    combined_sum = obj1.get_counter() + obj2.get_counter()
    end = time.time() - start
    print(f'multi process took: {end} seconds and summed to {combined_sum}')
    manager.shutdown()


if __name__ == '__main__':
    single_thread()
    multi_thread()
    multi_process()
