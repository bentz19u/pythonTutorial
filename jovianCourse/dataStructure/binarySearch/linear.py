from jovian.pythondsa import evaluate_test_case
from dictionaries.tests import tests

# We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order.
# We also need to minimize the number of times we access elements from the list.
# This is the brute force solution

# Edge cases
# The searched_number occurs somewhere in the middle of the list cards.
# searched_number is the first element in cards.
# searched_number is the last element in cards.
# The list cards contains just one element, which is searched_number.
# The list cards does not contain number searched_number.
# The list cards is empty.
# The list cards contains repeating numbers.
# The number searched_number occurs at more than one position in cards.

def locate_card(cards, searched_number):
    position = 0
    len_cards = len(cards)

    print('cards:', cards)
    print('searched_number:', searched_number)

    while position < len_cards:
        print('position:', position)

        if cards[position] == searched_number:
            return position

        position += 1
        if position == len_cards:
            return -1

    return -1

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(locate_card, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")

# ** automatically put the correct parameters from the dictionary
# result = locate_card(**test['input']) == test['output']
# print(result)

# Big O notation ; O(n) - linear time
