import itertools

permut = itertools.permutations(range(1, 7), 3)
count = 0

for perm in permut:
    print(perm)
    count += 1

print('number of permutations', count)
