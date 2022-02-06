from threading import Thread, Lock
import time


def thread_one(lock_one, lock_two):
    lock_one.acquire()
    print(f'thread_one acquired lock_one')
    time.sleep(1)
    lock_two.acquire()
    print(f'thread_one acquired lock_two')


def thread_two(lock_one, lock_two):
    lock_two.acquire()
    print(f'thread_two acquired two')
    time.sleep(1)
    lock_one.acquire()
    print(f'thread_two acquired lock_one')


lock_one = Lock()
lock_two = Lock()

Thread(target=thread_one, args=(lock_one, lock_two)).start()
Thread(target=thread_two, args=(lock_one, lock_two)).start()
