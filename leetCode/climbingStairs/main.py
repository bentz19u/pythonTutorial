from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


"""
Possible cases

1. 1 way
2. 2 way
3. x ways
"""

previousResult = {}


def climbStairs(n: int) -> int:
    if n in previousResult:
        return previousResult[n]

    total = 0
    if n > 2:
        total += climbStairs(n - 1)
        total += climbStairs(n - 2)

    if n == 1:
        total += 1

    if n == 2:
        total += 2

    if n not in previousResult:
        previousResult[n] = total

    return total


# result = evaluate_test_case(climbStairs, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(climbStairs, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
