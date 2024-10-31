from jovian.pythondsa import evaluate_test_case

from dictionnaries.tests import test, tests


# In an array, arr, the elements at indices and (where i < j) form an inversion if arr[i] > arr[j].
# In other words, inverted elements arr[i] and arr[j] are considered to be "out of order".
# To correct an inversion, we can swap adjacent elements.

# example of what kind of functions we are expecting (input and output)
def count_inversions_example(nums):
    # correct result for test case 1
    return 16


"""
Possible cases

1. generic case, there is a few inversions
2. no inversions, it's already sorted
3. the list is completely inversed
4. empty list
5. very long list
"""

def count_and_merge(left, right, num_inversions=0):
    idx_left, idx_right = 0, 0
    merged = []

    while idx_left < len(left) and idx_right < len(right):
        # left is lower than right, so no inversion
        if left[idx_left] <= right[idx_right]:
            merged.append(left[idx_left])
            idx_left += 1
        # right is lower, we need to inverse them
        else:
            merged.append(right[idx_right])
            num_inversions += len(left) - idx_left
            idx_right += 1

    # now one of the list maybe has numbers remaining
    left_tail = left[idx_left:]
    right_tail = right[idx_right:]

    return num_inversions, merged + left_tail + right_tail


def count_inversions(nums):
    def merge_sort_recursive(nums):
        # already sorted
        if len(nums) <= 1:
            return 0, nums

        mid = len(nums) // 2

        left = nums[:mid]
        right = nums[mid:]

        left_num_inversions, left_array = merge_sort_recursive(left)
        right_num_inversions, right_array = merge_sort_recursive(right)

        num_inversions = left_num_inversions + right_num_inversions

        num_inversions, sorted_nums = count_and_merge(left_array, right_array, num_inversions)

        # correct result for test case 1
        return num_inversions, sorted_nums

    num_inversions, sorted_nums = merge_sort_recursive(nums)

    return num_inversions


# result = evaluate_test_case(count_inversions, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(count_inversions, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")