from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

"""
Possible cases, guaranteed that s is a valid roman numeral

1. at index 0
2. doesnt exist
3. multiple occurrence of the string
4. empty string
"""


def strStr(haystack: str, needle: str) -> int:
    idx, max_idx = 0, len(haystack) - 1
    needle_len = len(needle)
    needle_start = needle[0]

    while idx <= max_idx:
        if haystack[idx] == needle_start:
            if haystack[idx:idx + needle_len] == needle:
                return idx
        idx += 1

    return -1


# result = evaluate_test_case(strStr, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(strStr, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
