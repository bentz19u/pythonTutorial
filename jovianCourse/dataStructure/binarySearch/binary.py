from jovian.pythondsa import evaluate_test_case
from dictionaries.tests import tests


# We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order.
# We also need to minimize the number of times we access elements from the list.

# Edge cases
# The searched_number occurs somewhere in the middle of the list cards.
# searched_number is the first element in cards.
# searched_number is the last element in cards.
# The list cards contains just one element, which is searched_number.
# The list cards does not contain number searched_number.
# The list cards is empty.
# The list cards contains repeating numbers.
# The number searched_number occurs at more than one position in cards.

def test_location(cards, searched_number, mid):
    if cards[mid] == searched_number:
        if mid - 1 >= 0 and cards[mid - 1] == searched_number:
            return 'left'
        else:
            return 'found'
    elif cards[mid] < searched_number:
        return 'left'
    else:
        return 'right'


def locate_card(cards, searched_number):
    low, high = 0, len(cards) - 1

    while low <= high:
        mid = (low + high) // 2

        result = test_location(cards, searched_number, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            high = mid - 1
        elif result == 'right':
            low = mid + 1

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

# Big O notation ; O(log N) - Binary search time

# A small exercise to get the first position and last position in an sorted list

# Python allow a function to be used as a parameter
def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid - 1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'left'
        else:
            return 'right'

    return binary_search(0, len(nums) - 1, condition)


def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums) - 1 and nums[mid + 1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'left'
        else:
            return 'right'

    return binary_search(0, len(nums) - 1, condition)


def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)


nums = [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
target = 6

result = first_and_last_position(nums, target)
print('first_and_last_position')
print(result)
