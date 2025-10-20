from typing import List

from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

"""
Possible cases

1. generic case
2. last number increase to next 10
"""


def plusOne(digits: List[int]) -> List[int]:
    full_int = 0
    for digit in digits:
        full_int = full_int * 10 + digit

    full_int += 1

    return list(map(int, str(full_int)))


# result = evaluate_test_case(plusOne, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(plusOne, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
