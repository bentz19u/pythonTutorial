from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.


"""
Possible cases

1. only ()
2. all cases in a row (not embed)
3. all embed cases
4. wrong case
5. parenthesis are ok but other are not
"""


def isValidOppositeSymbol(first: str, second: str) -> bool:
    if first == '(' and second == ')':
        return True
    if first == '[' and second == ']':
        return True
    if first == '{' and second == '}':
        return True
    return False


def isValid_old(s: str) -> bool:
    # we need to check the next position (direct closing) or the opposite position
    # if both are false, the string is invalid
    # once we reach half the string, we should know if it is valid or not
    # on another note, impair len means it will always be False
    idx, max_idx = 0, len(s) - 1

    while idx <= max_idx:
        # it should not be possible, that means there is only one char remaining
        if idx == max_idx:
            return False

        char = s[idx]
        next_char = s[idx + 1]
        if isValidOppositeSymbol(char, next_char):
            idx += 2
            continue

        opposite_char = s[max_idx]
        if isValidOppositeSymbol(char, opposite_char):
            idx += 1
            max_idx -= 1
            continue

        return False

    return True


# this time, let's used a stack
def isValid(s: str) -> bool:
    stack = []
    opening_char = ['(', '[', '{']

    for char in s:
        if char in opening_char:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False

            # get last item inserted in stack
            last_char = stack.pop()
            if not isValidOppositeSymbol(last_char, char):
                return False

    return not stack


# result = evaluate_test_case(isValid, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(isValid, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
