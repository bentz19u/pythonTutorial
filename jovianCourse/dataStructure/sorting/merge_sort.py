from jovian.pythondsa import evaluate_test_case
from dictionnaries.tests import tests, test, large_test


# write a function to do insertion sorting of a list of numbers in increasing order.
# example numbers = [4, 2, 6, 3, 4, 6, 2, 1]
# expected sorted array [1, 2, 2, 3, 4, 4, 6, 6]

# if the input list is empty or contains just one element, it is already sorted. Return it.
# if not, divide the list of numbers into two roughly equal parts.
# sort each part recursively using the merge sort algorithm. You'll get back two sorted lists.
# merge the two sorted lists to get a single sorted list

# first version
def merge_old(left_sorted, right_sorted):
    left_pointer, right_pointer = 0, 0
    sorted_array = []
    left_len = 0 if left_sorted is None else len(left_sorted)
    right_len = 0 if right_sorted is None else len(right_sorted)
    max_len = left_len + right_len

    # at each loop, we will check which value is the minimum at each pointer of the two arrays
    for i in range(max_len):
        left_value = None
        if left_pointer <= left_len - 1:
            left_value = left_sorted[left_pointer]

        right_value = None
        if right_pointer <= right_len - 1:
            right_value = right_sorted[right_pointer]

        if left_value is not None and right_value is None:
            sorted_array.append(left_value)
            left_pointer += 1
            continue
        elif left_value is None and right_value is not None:
            sorted_array.append(right_value)
            right_pointer += 1
            continue

        if left_value < right_value:
            sorted_array.append(left_value)
            left_pointer += 1
        else:
            sorted_array.append(right_value)
            right_pointer += 1

    return sorted_array


# new version more optimized/clean
def merge(left_sorted, right_sorted):
    merged = []
    i, j = 0, 0

    # loop over the two lists
    while i < len(left_sorted) and j < len(right_sorted):
        # include the smaller element in the result and move to next element
        if left_sorted[i] <= right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        else:
            merged.append(right_sorted[j])
            j += 1

    # get the remaining parts, one (or both) of them will be empty
    left_tail = left_sorted[i:]
    right_tail = right_sorted[j:]

    # return the final merged array
    return merged + left_tail + right_tail


def merge_sort(nums):
    # terminating condition (list of 0 or 1 elements)
    if len(nums) <= 1:
        return nums

    # get the midpoint
    mid = len(nums) // 2

    # split the list into two halves
    left = nums[:mid]
    right = nums[mid:]

    # solve the problem for each half recursively
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    # combine the results of the two halves
    sorted_nums = merge(left_sorted, right_sorted)

    return sorted_nums


is_all_tests_succeed = True
time_to_process = 0

# evaluate_test_case(merge_sort, test)

for test in tests:
    result = evaluate_test_case(merge_sort, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")

# testing the big test, faster than bubble or insertion sort
result = evaluate_test_case(merge_sort, large_test)
print(result)

# complexity of O(n log n)