from jovian.pythondsa import evaluate_test_case

from dictionnaries.tests import test, tests


# example of what kind of functions we are expecting (input and output)
def get_sub_array_given_sum(nums, target):
    # correct result for test case 1
    return [2, 5]


"""
Possible cases

1. generic array where the subarray is in the center
2. subarray is at the start
3. subarray is at the end
4. no subarray that match the target
5. there is a few zeros in the list
6. there is multiple sub arrays with the same sums
7. the array is empty
8. the subarray is a single element
"""


def get_sub_array_given_sum_brute_force(nums, target):
    length = len(nums)
    for i in range(0, length):
        for j in range(i + 1, length + 1):
            if sum(nums[i:j]) == target:
                # -1 because nums[i:j] exclude actually j, so we are calculating the index before
                return [i, j - 1]
            if sum(nums[i:j]) > target:
                break

    # not found
    return [None, None]


# result = evaluate_test_case(get_sub_array_given_sum_brute_force, test)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(get_sub_array_given_sum_brute_force, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
