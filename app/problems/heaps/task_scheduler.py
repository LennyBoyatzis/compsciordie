from collections import Counter
from queue import PriorityQueue, deque


def task_scheduler(tasks, n):
    task_counts = Counter(tasks)
    runq = PriorityQueue()
    waitq = deque()
    cpu_slots = []
    cycle = 0

    for task, freq in task_counts.items():
        runq.put((-freq, task))

    while not runq.empty() or waitq:
        if waitq:
            next_task = waitq[-1]
            is_task_ready = cycle - next_task[0] > n

            if is_task_ready:
                _, freq, task = waitq.pop()
                runq.put((freq, task))

        if not runq.empty():
            freq, task = runq.get()
            cpu_slots.append(task)
            if freq + 1 != 0:
                waitq.appendleft((cycle, freq+1, task))
        else:
            cpu_slots.append('idle')

        cycle += 1

    print(f'cpu_slots {cpu_slots}')
    return len(cpu_slots)


if __name__ == '__main__':
    cool_off_int = 2
    tasks = ['A', 'A', 'A', 'A', 'A',
             'A', 'B', 'C', 'D', 'E', 'F', 'G']
    # tasks = ['A', 'A', 'A', 'B', 'B', 'B']

    result = task_scheduler(tasks, cool_off_int)
    print(f'Result: {result} \n')
