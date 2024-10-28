from jovian.pythondsa import evaluate_test_case
from dictionnaries.tests import tests, test, large_test
import sys

# write a function to do insertion sorting of a list of numbers in increasing order.
# example numbers = [4, 2, 6, 3, 4, 6, 2, 1]
# expected sorted array [1, 2, 2, 3, 4, 4, 6, 6]

# if the list is empty or has just one element, return it. It's already sorted.
# pick a random element from the list. This element is called a pivot.
# reorder the list so that all elements with values less than or equal to the pivot come before the pivot,
# while all elements with values greater than the pivot come after it. This operation is called partitioning.
# the pivot element divides the array into two parts which can be sorted independently by making a recursive call to quicksort.

def partition(nums, start, end):
    if end is None:
        end = len(nums) - 1

    # initialize right and left pointers, pivot is last element so end - 1
    left, right = start, end - 1

    # iterate while they're apart
    while right > left:
        # print('  ', nums, l, r)
        # increment left pointer if number is less or equal to pivot
        if nums[left] <= nums[end]:
            left += 1

        # decrement right pointer if number is greater than pivot
        elif nums[right] > nums[end]:
            right -= 1

        # two out-of-place elements found, swap them
        else:
            nums[left], nums[right] = nums[right], nums[left]

    # place the pivot between the two parts
    if nums[left] > nums[end]:
        nums[left], nums[end] = nums[end], nums[left]
        return left
    else:
        return end

def quick_sort(nums, start=0, end=None):
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quick_sort(nums, start, pivot - 1)
        quick_sort(nums, pivot + 1, end)

    return nums

is_all_tests_succeed = True
time_to_process = 0

# evaluate_test_case(merge_sort, test)

for test in tests:
    result = evaluate_test_case(quick_sort, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")

default_limit = sys.getrecursionlimit()
sys.setrecursionlimit(20000)

# testing the big test, faster merge sort
# in this case, the large_test is terrible/unbalanced so the complexity will be O(n) which is the worst case
result = evaluate_test_case(quick_sort, large_test)
print(result)

sys.setrecursionlimit(default_limit)

# complexity of O(n log n)