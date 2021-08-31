import string

from typing import List
from collections import Counter 
# Subset | Subarray or Substring | Subsequence

# How to determine is S2 is a subset of S1
# Subset means all elements of S2 should be in S1
# Order does not matter
# No duplicates in S2

# n = length of s1
# m = length of s2
# O(m) time
# O(max(m,n)) is really just the same as O(m+n)


def is_subset(s1: str, s2: str) -> bool:
    """Determines if s2 is a subset of s1"""
    return set(s2).issubset(set(s1))


def is_subset_duplicates(s1: str, s2: str) -> bool:
    """Determines if s2 is a subset of s1, where s2 can contain duplicates"""
    counter_s1 = Counter(s1)
    counter_s2 = Counter(s2)
    diff = counter_s2 - counter_s1
    return len(diff) == 0


def is_substring(s1: str, s2: str) -> bool:
    """Determines if s2 is a substring of s1"""
    return s2 in s1


def is_subarray(s1: List[int], s2: List[int]) -> bool:
    """Determines if s2 is a subarray of s1"""
    i, j = 0, 0

    while i < len(s1) and j < len(s2):
        # If element matches
        # Increment both pointers
        if s1[i] == s2[j]:
            i += 1
            j += 1

            # if array s2 is completely traversed
            if j == len(s2):
                return True

        # If not, increment i and reset j
        else:
            i = i - j + 1
            j = 0
    return False


def is_subsequence(s1: str, s2: str) -> bool:
    """Determines if s2 is a subsequence of s1"""
    it = iter(s1)
    return all(c in it for c in s2)



if __name__ == '__main__':
    s1 = [2, 3, 0, 5, 1, 1, 2] 
    s2 = [3, 0, 5, 1] 

    s1 = string.ascii_lowercase
    s2 = 'dae'

    res = is_subsequence(s1, s2)
    print(f'res {res}')
