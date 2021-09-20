def staircase_traversal_global(height, max_steps):
    ways = 0

    def traverse(amount):
        nonlocal ways

        if amount < 0:
            return

        if amount == 0:
            ways += 1
            return
        elif amount > 0:
            for i in range(1, max_steps+1):
                traverse(amount-i)

    traverse(height)
    return ways


def memoize(fn):
    cache = {}

    def inner(height, max_steps):
        if height in cache:
            return cache[height]
        else:
            cache[height] = fn(height, max_steps)
            return cache[height]
    return inner


@memoize
def traverse(height, max_steps):
    if height <= 1:
        return 1

    number_of_ways = 0
    for step in range(1, min(max_steps, height) + 1):
        number_of_ways += traverse(height - step, max_steps)

    return number_of_ways



if __name__ == '__main__':
    height = 10 
    max_steps = 1 

    res = traverse(height, max_steps)
    print(f'res {res}')
