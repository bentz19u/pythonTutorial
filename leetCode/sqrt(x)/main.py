from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
#
# You must not use any built-in exponent function or operator.
#
#     For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


"""
Possible cases

1. square root is an int
2. square root is a decimal
"""


def mySqrt(x: int) -> int:
    # the idea is to guess what will be the square root,
    # then when the difference between the guessed root (g) multiplied by itself is very closed to x, it's good
    g = x / 2
    while abs(g * g - x) > 0.0001:
        g = 0.5 * (g + x / g)

    return int(g)


result = evaluate_test_case(mySqrt, test)
print(result)

# is_all_tests_succeed = True
# time_to_process = 0
#
# for test in tests:
#     result = evaluate_test_case(mySqrt, test)
#     time_to_process += result[2]
#
#     # index 1 has a boolean if the test worked or not
#     if not result[1]:
#         is_all_tests_succeed = False
#
# print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
