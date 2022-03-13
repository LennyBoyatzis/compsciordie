from collections import defaultdict


"""
Design a stack-like data structure to push elements to the stack
and op the most frequent element from the stack

- pop() - removes most frequent element in the stack. If tie
the element closest to the stack's top is removed and returned
"""


class FreqStack:
    def __init__(self):
        self.stack = defaultdict(list) 
        self.counts = defaultdict(int) 
        self.max_freq = 0

    def push(self, val):
        self.counts[val] += 1
        val_count = self.counts[val]

        if val_count > self.max_freq:
            self.max_freq = val_count

        self.stack[val_count].append(val)

    def pop(self):
        val = self.stack[self.max_freq].pop()
        self.counts[val] -= 1 

        if len(self.stack[self.max_freq]) == 0:
            self.max_freq -= 1

        return val


if __name__ == '__main__':
    stack = FreqStack()

    stack.push(5)
    stack.push(7)
    stack.push(5)
    stack.push(7)
    stack.push(4)
    stack.push(5)

    print(stack.pop()) # 5
    print(stack.pop()) # 7 
    print(stack.pop()) # 5 
    print(stack.pop()) # 4 
