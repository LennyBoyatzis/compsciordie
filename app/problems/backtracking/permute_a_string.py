"""
Given a string, print all permutations

- Complete Search (Exhaustive/Brute Force Search)
- This is a backtracking problem
"""


def permute(string):
    permutations = []
    if len(string) == 1:
        permutations.append(string)
    else:
        for index, char in enumerate(string):
            substring = string[:index] + string[index+1:]
            for perm in permute(substring):
                permutations.append(char + perm)
    return permutations


if __name__ == '__main__':
    text = "abc"
    result = permute(text)
    print(f'result {result}')
