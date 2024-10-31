from jovian.pythondsa import evaluate_test_case

from dictionnaries.tests import test, tests


# Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)
# You have the following 3 operations permitted on a word:
# example of what kind of functions we are expecting (input and output)
def min_steps_example(str1, str2):
    # correct result for test case 1
    return 5

"""
Possible cases

1. generic case, two works with same length
2. no change is required
3. all the characters need to be changed
4. unequal length
5. one of the string is empty
6. only deletion
7. only addition
8. only swapping
"""

"""
Recursion:
- if the first char is equal, then ignore from both
- if the first char is not equal:
    - either it has to be deleted
        - 1 + recursively solve after ignoring first char of str1
    - or swapped
        - 1 + recursively solve after ignoring first char of both str
    - or it has to be inserted
        - 1 + recursively solve after ignoring first char of str2
"""

def min_steps(str1, str2, idx1 = 0, idx2 = 0):
    # case where either one of the string has reached the end but the other has not
    if idx1 == len(str1):
        return len(str2) - idx2
    elif idx2 == len(str2):
        return len(str1) - idx1

    number_step = 0
    if idx1 < len(str1) and idx2 < len(str2):
        if str1[idx1] == str2[idx2]:
            number_step = min_steps(str1, str2, idx1 + 1, idx2 + 1)
        else:
            delete_option = 1 + min_steps(str1, str2, idx1 + 1, idx2)
            swap_option = 1 + min_steps(str1, str2, idx1 + 1, idx2 + 1)
            insert_option = 1 + min_steps(str1, str2, idx1, idx2 + 1)
            number_step = min(delete_option, swap_option, insert_option)

    return number_step

# result = evaluate_test_case(min_steps, test)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(min_steps, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
# Complexity of O(3^min(m*n))

def min_steps_memo(str1, str2):
    memo = {}
    def recurse(idx1 = 0, idx2 = 0):
        key = (idx1, idx2)
        if key in memo:
            return memo[key]

        if idx1 == len(str1):
            memo[key] = len(str2) - idx2
        elif idx2 == len(str2):
            memo[key] = len(str1) - idx1
        elif idx1 < len(str1) and idx2 < len(str2):
            if str1[idx1] == str2[idx2]:
                memo[key] = recurse(idx1 + 1, idx2 + 1)
            else:
                delete_option = 1 + recurse(idx1 + 1, idx2)
                swap_option = 1 + recurse(idx1 + 1, idx2 + 1)
                insert_option = 1 + recurse(idx1, idx2 + 1)
                memo[key] = min(delete_option, swap_option, insert_option)

        return memo[key]

    return recurse()

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(min_steps_memo, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
# Complexity of O(m*n)