from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# You are planning production for an order.
# You have a number of machines that each have a fixed number of days to produce an item.
# Given that all the machines operate simultaneously,
# determine the minimum number of days to produce the required order.

# For example, you have to produce goal = 10 items.
# You have three machines that take machines = [2,3,2] days to produce an item.
# The following is a schedule of items produced:

# Day Production  Count
# 2   2               2
# 3   1               3
# 4   2               5
# 6   3               8
# 8   2              10

# It takes 10 days to produce items using these machines.

# Complete the minTime function below.
def minTimeExample(machines, goal):
    return 6

def minTimeBruteForce(machines, goal):
    found = False
    days = 1
    while not found:
        total_machines = 0
        for i in machines:
            total_machines += days // i

        if total_machines >= goal:
            found = True
        else:
            days += 1

    return days

def minTime(machines, goal):
    machines.sort()
    low = 1
    high = machines[-1] * goal
    minimum_time = high

    while low <= high:
        mid = (low + high) // 2

        total_products = 0
        for i in machines:
            total_products += mid // i

        if total_products >= goal:
            minimum_time = mid
            high = mid - 1
        else:
            low = mid+1

    return minimum_time


# result = evaluate_test_case(minTime, test)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(minTime, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")