from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# Given a string s, find the length of the longest without duplicate characters.

"""
Possible cases

1. generic case
2. same letter repeated
3. empty string
"""


# not optimal, kinda brute forced
def lengthOfLongestSubstringOld(s: str) -> int:
    my_set = set()
    idx1, idx2, max_idx = 0, 1, len(s) - 1

    # make a list of all subset
    while idx1 <= max_idx:
        my_set.add(s[idx1:idx2])

        if idx2 <= max_idx:
            idx2 += 1
        else:
            idx1 += 1
            idx2 = idx1 + 1

    # then check them one by one to find out the max len
    max_len = 0
    for value in my_set:
        list_char = []
        valid_string = True

        for key, char in enumerate(value):
            if char in list_char:
                valid_string = False
                continue
            list_char.append(char)

        if valid_string and len(value) > max_len:
            max_len = len(value)

    return max_len


def lengthOfLongestSubstringBetterVersion(s: str) -> int:
    my_set = set()
    idx1, idx2, max_idx = 0, 1, len(s) - 1

    # array empty
    if max_idx < 0:
        return 0

    # one char only
    if max_idx == 0:
        return 1

    current_len, max_len = 1, 1
    my_set.add(s[idx1])
    while idx2 <= max_idx:
        # char is already in list, we reset
        if s[idx2] in my_set:
            idx1 += 1
            idx2 = idx1 + 1
            current_len = 1

            my_set.clear()
            my_set.add(s[idx1])
            continue

        # char is not in the list, we continue
        my_set.add(s[idx2])
        idx2 += 1

        current_len += 1
        if current_len > max_len:
            max_len = current_len

    return max_len


# optimal version
def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        # if we find a duplicate, move left until it’s gone
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        # add the current char and update max length
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


result = evaluate_test_case(lengthOfLongestSubstring, test)
print(result)

# is_all_tests_succeed = True
# time_to_process = 0
#
# for test in tests:
#     result = evaluate_test_case(lengthOfLongestSubstring, test)
#     time_to_process += result[2]
#
#     # index 1 has a boolean if the test worked or not
#     if not result[1]:
#         is_all_tests_succeed = False
#
# print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
