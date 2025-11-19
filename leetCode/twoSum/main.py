from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

"""
Possible cases

1. generic case
2. first two elements are the answer
3. last two elements are the answer
"""


# easiest solution would be to sort the array first and then check both end of it one by one
def two_sum_old(nums, target):
    index_map = {}

    for idx, num in enumerate(nums):
        if num not in index_map:
            index_map[num] = []
        index_map[num].append(idx)

    sorted_array = sorted(nums)

    idx1, idx2 = 0, len(sorted_array) - 1

    while idx1 < idx2:
        sum = sorted_array[idx1] + sorted_array[idx2]

        if sum == target:
            result_idx1 = index_map[sorted_array[idx1]][0]

            index_map[sorted_array[idx1]].pop(0)

            result_idx2 = index_map[sorted_array[idx2]][0]

            return [result_idx1, result_idx2]

        if sum > target:
            idx2 -= 1
        else:
            idx1 += 1


def two_sum(nums, target):
    index_map = {}

    for idx, num in enumerate(nums):
        difference = target - num
        if difference in index_map:
            return [index_map[difference], idx]

        index_map[num] = idx


# result = evaluate_test_case(two_sum, test)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(two_sum, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
