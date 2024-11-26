# Given an array of integers, sort the array in ascending order using the
# Bubble Sort algorithm above. Once sorted, print the following three lines:
# 1: Array is sorted in numSwaps swaps., where is the number of swaps that took place.
# 2: First Element: firstElement, where is the first element in the sorted array.
# 3: Last Element: lastElement, where is the last element in the sorted array.

"""
Possible cases

1. generic case
2. array already sorted
3. empty array
4. same numbers exists in the array
"""

def count_swaps(unsorted_array):
    number_swaps = 0
    length = len(unsorted_array)

    is_sorted = False

    while not is_sorted:
        is_swap = False
        for i in range(length - 1):
            if unsorted_array[i] > unsorted_array[i + 1]:
                unsorted_array[i], unsorted_array[i + 1] = unsorted_array[i + 1], unsorted_array[i]
                is_swap = True
                number_swaps += 1

        if not is_swap:
            is_sorted = True

    print(f'Array is sorted in {number_swaps} swaps.')
    print(f'First Element: {unsorted_array[0]}')
    print(f'Last Element: {unsorted_array[length - 1]}')


test = [6, 4, 1]
count_swaps(test)
