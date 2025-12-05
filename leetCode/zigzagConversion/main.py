from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# And then read line by line: "PAHNAPLSIIGYIR"

"""
Possible cases

1. small input
2. one string with 3 num rows
3. same string with 4 num rows
"""


def convert_old(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    # we will generate the 2D array here
    matrix = {}
    col, row = 0, 0
    max_col = 0

    len_s = len(s) - 1
    current = 0
    pattern = 'down'
    while current <= len_s:
        if pattern == 'down':
            matrix[(col, row)] = s[current]

            if row >= numRows - 1:
                pattern = 'zigzag'
                col += 1
                row -= 1
            else:
                row += 1
        else:
            matrix[(col, row)] = s[current]

            if row <= 0:
                pattern = 'down'
                row += 1
            else:
                col += 1
                row -= 1

        if max_col < col:
            max_col = col

        current += 1

    output = ''

    col, row = 0, 0
    current = 0
    while current <= len_s:
        if (col, row) in matrix:
            output += matrix[(col, row)]
            current += 1

        if col <= max_col:
            col += 1
        else:
            col = 0
            row += 1

    return output


# optimized version, I keep the value in a array of strings instead of a matrix(dict)
def convert(s: str, numRows: int) -> str:
    rows = [''] * numRows

    current, height = 0, 0
    pattern = 'down'
    while current <= len(s) - 1:
        rows[height] += s[current]
        current += 1

        if numRows == 1:
            continue

        if height == numRows - 1:
            pattern = 'up'
        elif height == 0:
            pattern = 'down'

        height += -1 if pattern == 'up' else 1

    output = ''
    for row in rows:
        output += row

    return output


# result = evaluate_test_case(convert, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(convert, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
