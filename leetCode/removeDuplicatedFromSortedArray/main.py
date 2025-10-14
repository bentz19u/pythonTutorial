from typing import List

from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
#
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#     Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
#     Return k.


"""
Possible cases

1. small list
2. large list
3. empty list
4. input and output are the same
"""


# first version, it can be improved easily
def removeDuplicates(nums: List[int]) -> int:
    numbers_found = {}
    index_to_delete = []

    for index, num in enumerate(nums):
        if num not in numbers_found:
            numbers_found[num] = num
        else:
            index_to_delete.append(index)

    for index in reversed(index_to_delete):
        del (nums[index])

    return len(nums)


# result = evaluate_test_case(removeDuplicates, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(removeDuplicates, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
