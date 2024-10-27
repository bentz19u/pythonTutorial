from jovian.pythondsa import evaluate_test_case
from dictionnaries.tests import tests, test, large_test

# write a function to buble sorting of a list of numbers in increasing order.
# example numbers = [4, 2, 6, 3, 4, 6, 2, 1]
# expected sorted array [1, 2, 2, 3, 4, 4, 6, 6]

def bubble_sort(nums):
    # it seems that in python, every parameter are in ref
    nums = list(nums)

    # by default, it is not sorted
    is_sorted = False
    while not is_sorted:
        # we will turn it to false if the for loop trigger a swap at least once
        is_swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                is_swapped = True

        if not is_swapped:
            is_sorted = True

    return nums

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(bubble_sort, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")

# testing the big test, commented because it's too long, roughly 8 sec
# result = evaluate_test_case(bubble_sort, large_test)
# print(result)

# complexity of O(n2)