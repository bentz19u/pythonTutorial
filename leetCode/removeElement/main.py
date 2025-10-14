from typing import List

from jovian.pythondsa import evaluate_test_case

from tests import test, tests

from leetCode.listNode import ListNode

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed.
# Then return the number of elements in nums which are not equal to val.
#
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
#
#     Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
#     Return k.


"""
Possible cases

1. generic case
1. larger list
2. no element to remove
3. empty list
"""


def removeElement(nums: List[int], val: int) -> int:
    read, write = len(nums) - 1, len(nums) - 1

    removed_count = 0
    while read >= 0:
        if nums[read] == val:
            keep_safe = nums[write]
            nums[write] = nums[read]
            nums[read] = keep_safe
            write -= 1
            removed_count += 1

        read -= 1

    return len(nums) - removed_count


# result = evaluate_test_case(removeElement, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(removeElement, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
