from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# Given an integer x, return true if x is a palindrome, and false otherwise.

"""
Possible cases

1. generic case, positive
2. generic case, negative
3. number is negative
4. number is 0
"""


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False

    if x == 0:
        return True

    str_x = str(x)

    idx1, idx2 = 0, len(str_x) - 1

    while idx1 < idx2:
        if str_x[idx1] == str_x[idx2]:
            idx1 += 1
            idx2 -= 1
            continue
        else:
            return False

    return True


# result = evaluate_test_case(is_palindrome, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(is_palindrome, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
