from jovian.pythondsa import evaluate_test_case
from dictionnaries.tests import tests, test, large_test

# write a function to do insertion sorting of a list of numbers in increasing order.
# example numbers = [4, 2, 6, 3, 4, 6, 2, 1]
# expected sorted array [1, 2, 2, 3, 4, 4, 6, 6]

# the idea is to check the number one by one
# and place then at their correct position depending on the first portion of array already sorted

def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1
        while j >=0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(insertion_sort, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")

# testing the big test, commented because it's too long, roughly 8 sec
result = evaluate_test_case(insertion_sort, large_test)
print(result)