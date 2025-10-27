from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# Given two binary strings a and b, return their sum as a binary string.

"""
1+1=0 with carry 1
1+0=1 with carry 0
0+1=1 with carry 0
0+0=0 with carry 0
Imp:1+1=1 with carry 1 if previous carry was 1.
The carry gets added in next step(scanning from right to left).
"""


def addBinary(a: str, b: str) -> str:
    a_len = len(a) - 1
    b_len = len(b) - 1
    carry = 0
    result = ""

    while a_len >= 0 or b_len >= 0 or carry:
        total = carry
        if a_len >= 0:
            total += int(a[a_len])
            a_len -= 1
        if b_len >= 0:
            total += int(b[b_len])
            b_len -= 1

        result = str(total % 2) + result
        carry = total // 2

    return result


result = evaluate_test_case(addBinary, test)
print(result)

# is_all_tests_succeed = True
# time_to_process = 0
#
# for test in tests:
#     result = evaluate_test_case(addBinary, test)
#     time_to_process += result[2]
#
#     # index 1 has a boolean if the test worked or not
#     if not result[1]:
#         is_all_tests_succeed = False
#
# print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
