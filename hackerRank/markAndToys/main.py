from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# Calculate the maximum number of toys we can buy depending on our budgets

"""
Possible cases

1. generic case
2. out budget is not enough to buy anything
3. we are so rich we can buy everything
4. list of toys is empty
5. large test?
"""
# [1, 12, 5, 111, 200, 1000, 10], 50

def maximumToysExample(prices, k):
    return 4

def maximumToys(prices, k):
    sorted_array = sorted(prices)
    idx, items, total = 0, 0, 0
    while idx < len(sorted_array):
        total += sorted_array[idx]
        if total > k:
            return items
        items += 1
        idx += 1

    return items

# result = evaluate_test_case(maximumToysExample, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(maximumToys, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")