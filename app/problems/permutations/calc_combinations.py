import itertools

combos = itertools.combinations(range(1, 7), 3)
count = 0

for combo in combos:
    print(combo)
    count += 1

print('number of combinations', count)
