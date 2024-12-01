from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# In an array,arr, the elements at indices i and j (where i < j) form an inversion if arr[i] > arr[j].
# In other words, inverted elements arr[i] and arr[j] are considered to be "out of order".
# To correct an inversion, we can swap adjacent elements.

# example
# arr = [2,4,1], r = 2
# The sort has two inversions: (4,1) and (2,1).


"""
Possible cases

1. generic case
2. already sorted
3. all same values
4. sorted but in descending order
5. very big list
"""


# example of what kind of functions we are expecting (input and output)
def countInversionsExample(arr):
    # correct result for test case 1
    return 4


# brute force version
def countInversionsBrutForce(arr):
    swap_count = 0
    length = len(arr)

    idx1, idx2 = 0, 1
    while idx1 < length - 1:

        if arr[idx1] > arr[idx2]:
            print(f"idx1 {idx1}, idx2 {idx2}")
            remove_element = arr.pop(idx2)
            arr.insert(idx1, remove_element)
            swap_count += idx2 - idx1

        idx2 += 1

        if idx2 > (length - 1):
            idx1 += 1
            idx2 = idx1 + 1

    return swap_count


def merge(left, right):
    swap_count = 0
    sorted_array = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            sorted_array.append(left[left_idx])
            left_idx += 1
        else:
            sorted_array.append(right[right_idx])
            right_idx += 1
            swap_count += len(left) - left_idx

    # get the remaining parts, one (or both) of them will be empty
    left_tail = left[left_idx:]
    right_tail = right[right_idx:]

    return sorted_array + left_tail + right_tail, swap_count


def countInversions(arr):
    def recursive(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2

        left_arr = arr[:mid]
        right_arr = arr[mid:]

        left_sorted, left_inversions = recursive(left_arr)
        right_sorted, right_inversions = recursive(right_arr)

        sorted_array, merge_inversions = merge(left_sorted, right_sorted)

        total_inversions = left_inversions + right_inversions + merge_inversions

        return sorted_array, total_inversions

    _, total_inversions = recursive(arr)

    return total_inversions


# result = evaluate_test_case(countInversions, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(countInversions, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
