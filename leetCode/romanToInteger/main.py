from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
#     I can be placed before V (5) and X (10) to make 4 and 9.
#     X can be placed before L (50) and C (100) to make 40 and 90.
#     C can be placed before D (500) and M (1000) to make 400 and 900.
#
# Given a roman numeral, convert it to an integer.

"""
Possible cases, guaranteed that s is a valid roman numeral

1. simple case less than 10
2. case with more than 10
3. case with special combination
"""


def romanToInt(s: str) -> int:
    cases = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10,
             "XL": 40, "L": 50, "XC": 90,
             "C": 100, "CD": 400, "D": 500,
             "CM": 900, "M": 1000}

    idx = 0
    max_idx = len(s) - 1
    total = 0

    while idx <= max_idx:
        if idx != max_idx:
            double_str = s[idx] + s[idx + 1]
            if double_str in cases:
                total += cases[double_str]
                idx += 2
                continue

        total += cases[s[idx]]
        idx += 1

    return total


# result = evaluate_test_case(romanToInt, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(romanToInt, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
