from typing import List

from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# useful constraints = 1 <= strs.length <= 200

"""
Possible cases

1. generic case, prefix exist
2. generic case, no common prefix
3. lot of words
4. empty array
"""


def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""

    # first get the minimum string length in the list, that will be our max index
    min_length = min(len(word) for word in strs)

    # then check each index of each words to see if they match
    common_prefix = ''
    should_continue = True
    for idx in range(min_length):
        # no need to continue, we already know they won't match
        if not should_continue:
            break

        # we get the string of the first word
        current_str = strs[0][0:idx + 1]
        for word in strs:
            if current_str != word[0:idx + 1]:
                should_continue = False
                break

        # we reached the last word without issue so we keep the common string
        if should_continue:
            common_prefix = current_str

    # return the last matching string when an error is found
    return common_prefix


# result = evaluate_test_case(longestCommonPrefix, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(longestCommonPrefix, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
