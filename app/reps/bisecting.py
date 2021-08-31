import bisect

# dir(bisect)
# bisect
# bisect_left
# bisect_right
# insort
# insort_left
# insort_right


def test_bisect(arr):
    sorted_arr = sorted(arr) # [-20, 1, 2, 12, 19, 44]

    # NOTE: No Duplicates Scenario
    # If element to be inserted has a clear position bisect, bisect_left, bisect_right are all the same
    # i.e. instance in which there is no duplication of elements
    bisect.bisect(sorted_arr, 10) # 3, index position of where element would be inserted
    bisect.bisect_left(sorted_arr, 10) # 3, index position of where the element would be inserted
    bisect.bisect_right(sorted_arr, 10) # 3, index position of where the element would be inserted

    # NOTE: Duplicates Scenario
    duplicates_arr = [1, 1, 2, 2, 2, 2, 3, 7, 12]
    bisect.bisect(duplicates_arr, 10) # 6, defaults to bisect right 
    bisect.bisect_left(duplicates_arr, 10) # 2, index position of where the element would be inserted
    bisect.bisect_right(duplicates_arr, 10) # 6, index position of where the element would be inserted


def test_insort(arr):
    sorted_arr = sorted(arr) # [-20, 1, 2, 12, 19, 44]

    # NOTE: No Duplicates Scenario
    # If element to be inserted has a clear position bisect, bisect_left, bisect_right are all the same
    bisect.insort(sorted_arr, 10) # [-20, 1, 2, 10, 12, 19, 44]
    bisect.bisect_left(sorted_arr, 10)  # [-20, 1, 2, 10, 12, 19, 44]
    bisect.bisect_right(sorted_arr, 10) # [-20, 1, 2, 10, 12, 19, 44]

    # NOTE: Duplicates Scenario
    duplicates_arr = [1, 1, 2, 2, 2, 2, 3, 7, 12]
    bisect.insort(duplicates_arr, 10) # [1, 1, 2, 2, 2, 2, "--2--", 3, 7, 12] # defaults to insort_right
    bisect.insort_left(duplicates_arr, 10) # [1, 1, "--2--", 2, 2, 2, 2, 3, 7, 12]
    bisect.insort_right(duplicates_arr, 10) # [1, 1, 2, 2, 2, 2, "--2--", 3, 7, 12]


if __name__ == '__main__':
    arr = [1, 2, -20, 19, 44, 12] 
