from typing import List

from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.


"""
Possible cases

1. target exist
2. target does not exist and should be somewhere in the middle
3. target doesnt not exist and should be at the end
"""


def searchInsert(nums: List[int], target: int, idx_start=0, idx_end=None) -> int:
    if idx_end == None:
        idx_end = len(nums) - 1

    # last recursivity
    if idx_start > idx_end:
        return idx_start

    mid = idx_start + (idx_end - idx_start) // 2

    if target == nums[mid]:
        return mid
    elif target < nums[mid]:
        return searchInsert(nums, target, idx_start, mid - 1)
    else:
        return searchInsert(nums, target, mid + 1, idx_end)


# result = evaluate_test_case(searchInsert, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(searchInsert, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
