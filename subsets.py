import string
from collections import Counter


alphabet = string.ascii_lowercase
subset = 'deflmnoab' # subset and subsequence NOT substring or subarray


# Can't be duplicates in the candidate
def is_subset(text, candidate):
    """Returns true if candidate with distinct elements is subset of text"""
    set_text = set(text)
    set_candidate = set(candidate)
    return set_candidate.issubset(set_text)


# Can have duplicates in the candidate
def is_subset_with_duplicates(text, candidate):
    """Returns true if candidate without distinct elements is subset of text"""
    counter_text = Counter(text)
    counter_candidate = Counter(candidate)
    diff = counter_candidate - counter_text
    return len(diff) == 0


# All chars in candidate must appear in same order in text, don't have to be contiguous
def is_subsequence(text, candidate):
    """Returns true if candidate is a subsequence of text"""
    it = iter(text)
    results = [char in it for char in candidate]
    print(f'results {results}')
    return all(results)
    

# res = is_subset(alphabet, subset)
# print(f'is_subset {res}') # True

# res = is_subset_with_duplicates(alphabet, subset*2)
# print(f'is_subset_with_duplicates {res}') # False

res = is_subsequence(alphabet, subset)
print(f'is_subsequence {res}') # True


# it = iter([1, 2, 3, 4])

# for x in it:
#     print(f'x-first: {x}')
#     break

# for x in it:
#     print(f'x-second: {x}')

# print('done')



