from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal
# consisting of non-space characters only.

"""
Possible cases

1. generic case
2. space at the end
"""


def lengthOfLastWord(s: str) -> int:
    idx = len(s) - 1
    word_found = False
    len_word = 0
    while 0 <= idx:
        # return result
        if word_found and s[idx] == ' ':
            return len_word

        if not word_found and s[idx] == ' ':
            idx -= 1
            continue

        if not word_found and s[idx] != ' ':
            word_found = True

        len_word += 1
        idx -= 1

    return len_word


# result = evaluate_test_case(lengthOfLastWord, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(lengthOfLastWord, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
