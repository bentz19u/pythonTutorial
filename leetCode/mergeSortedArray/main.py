from typing import List

from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


"""
Possible cases

1. X element to move from array 2 to 1
2. array 2 is empty
3. array 1 has only 0 numbers
"""


# test = {'input': {'nums1': [1, 2, 4, 5, 6, 0], 'm': 5, 'nums2': [3], 'n': 1}, 'output': [1, 2, 3, 4, 5, 6]}

# first version, it can be improved easily
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    current = len(nums1) - 1
    idx1, idx2 = m - 1, n - 1

    while current >= 0:
        if idx2 >= 0 and (idx1 < 0 or nums2[idx2] >= nums1[idx1]):
            nums1[current] = nums2[idx2]
            idx2 -= 1

        elif idx1 >= 0:
            nums1[current] = nums1[idx1]
            idx1 -= 1

        current -= 1

    return nums1


# result = evaluate_test_case(merge, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(merge, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
