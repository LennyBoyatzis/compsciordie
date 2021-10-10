import statistics

def quicksort(nums):
    if len(nums) <= 1:
        return numbers
    else:
        pivot = statistics.median(
            [
                numbers[0],
                numbers[len(numbers) // 2],
                numbers[-1]
            ])

        items_less, pivot_items, items_greater = (
            [n for n in numbers if n < pivot],
            [n for n in numbers if n == pivot],
            [n for n in numbers if n > pivot])

        return (
            quicksort(items_less) + 
            pivot_items +
            quicksort(items_greater))
