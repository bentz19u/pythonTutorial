from jovian.pythondsa import evaluate_test_case
from dictionaries.tests import rotated_tests


# a list of sorted numbers has been rotated a few times by removing the last element of adding it before the first element
# output should be the number of time the list has been rotated

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid, hi)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def find_number_rotation(nums):
    # we cannot define any number of rotation if there is no element or only one
    if len(nums) in [0, 1]:
        return -1

    # edge case when the array has not been rotated
    if nums[0] < nums[len(nums) - 1]:
        return 0

    def condition(mid, hi):
        if nums[mid + 1] < nums[mid]:
            return 'found'
        elif nums[mid] < nums[hi]:
            return 'left'
        else:
            return 'right'

    result = binary_search(0, len(nums) - 1, condition)
    # error
    if (result == -1):
        return -1
    else:
        return result + 1  # index start at 0


# evaluate_test_case(find_number_rotation, rotated_test)

is_all_tests_succeed = True
time_to_process = 0

for test in rotated_tests:
    result = evaluate_test_case(find_number_rotation, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
