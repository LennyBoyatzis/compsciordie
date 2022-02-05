class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, val):
        stack.append(val)

    def pop(self):
        stack.pop()


def reverse_stack(stack):
    """Reverses a stack"""
    if not stack.is_empty():
        el = stack.pop()
        reverse_stack(stack)






    pass


if __name__ == '__main__':
    nums = [8, 5, 3, 2] # 8 is top
    stack = Stack()

    for i in range(len(nums)-1, -1, -1):
        stack.push(nums[i])

    res = reverse_stack(stack)
    expected = [2, 3, 5, 8] 

    print(f'res {res}')
    assert res == expected 
