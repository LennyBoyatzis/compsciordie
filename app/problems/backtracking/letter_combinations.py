"""
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

"""
Backtracking is an algorithm for finding all solutions by exploring all
potential candidates

If the solution candidate turns to be not a solution, backtracking algorithm
discards it and makes some changes to the previous step

N = number of digits in the input which maps to 3 letters only (2, 3, 4, 5, 6, 8)
M = number of digits in the input which maps to 4 letters only (7, 9)

Time: O(3^N x 4^M)
Space: O(3^N x 4^M)
"""


def letter_combinations(digits):
    phone = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'}

    output = []

    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            output.append(combination)
        else:
            letters = phone[next_digits[0]]
            for letter in letters:
                backtrack(combination + letter, next_digits[1:])

    if digits:
        backtrack('', digits)
    return output


if __name__ == '__main__':
    digits = '23'
    results = letter_combinations(digits)
    print(f'results {results}')
