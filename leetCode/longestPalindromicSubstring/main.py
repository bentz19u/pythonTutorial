from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# Given a string s, return the longest palindromic substring in s

"""
Possible cases

1. palindrome is in the beginning
2. palindrome is in the center
3. s has one char
4. long string
"""

memo = {}


def is_palindrome(s: str, idx1: int, idx2: int) -> bool:
    if s == '':
        return True

    while idx1 < idx2:
        if s[idx1] == s[idx2]:
            idx1 += 1
            idx2 -= 1
            continue
        else:
            return False

    return True


def longestPalindrome(s: str, idx1=None, idx2=None) -> str:
    if idx1 is None:
        idx1, idx2 = 0, len(s) - 1

    key = (idx1, idx2)

    if key in memo:
        return memo[key]

    if is_palindrome(s, idx1, idx2):
        memo[key] = s[idx1:idx2 + 1]
        return memo[key]

    res1 = longestPalindrome(s, idx1, idx2 - 1)
    res2 = longestPalindrome(s, idx1 + 1, idx2)

    final_res = res1 if len(res1) > len(res2) else res2

    memo[key] = final_res

    return final_res


result = evaluate_test_case(longestPalindrome, test)
print(result)

# is_all_tests_succeed = True
# time_to_process = 0
#
# for test in tests:
#     result = evaluate_test_case(longestPalindrome, test)
#     time_to_process += result[2]
#
#     # index 1 has a boolean if the test worked or not
#     if not result[1]:
#         is_all_tests_succeed = False
#
# print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
