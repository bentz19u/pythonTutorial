from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

"""
Possible cases

1. positive input
2. negative input
3. number end with 0
4. output is out of bound
"""


def reverse(x: int) -> int:
    x_reversed = ''
    if x < 0:
        x_reversed = '-'

    x_str = str(abs(x))
    current = len(x_str) - 1

    while current >= 0:
        x_reversed += x_str[current]
        current -= 1

    x_reversed = int(x_reversed)

    if x_reversed < -2147483648 or x_reversed > 2147483647:
        return 0

    return x_reversed


#
# result = evaluate_test_case(reverse, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(reverse, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
