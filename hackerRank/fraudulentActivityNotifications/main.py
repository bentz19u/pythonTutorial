
import bisect
from jovian.pythondsa import evaluate_test_case

from tests import test, tests

# HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity
# If the amount spent by a client on a particular day is greater than or equal to 2x the client's median spending for a trailing number of days,
# they send the client a notification about potential fraud.
# The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.
# Given the number of trailing d days and a client's total daily expenditures for a period of days,
# determine the number of times the client will receive a notification over all n days.
# Example
# expenditure = [10,20,30,40,50]
# d = 3
# On the first three days, they just collect spending data. At day 4, trailing expenditures are [10,20,30].
# The median is 20 and the day's expenditure is 40.
# Because 40 >= 2 * 20, there will be a notice.
# The next day, trailing expenditures are [20,30,40] and the expenditures are 50.
# This is less than 2*30 so no notice will be sent. Over the period, there was one notice sent.

"""
Possible clases

1. generic case with notifications
2. generic case with no notification
3. d bigger than the number of cases
4. d at 0?
5. d at 1?
6. very long expenditure and d

"""


def activityNotificationsExample(expenditure, d):
    return 2

def calculate_median(freq, d):
    count, first, second = 0, None, None
    for i, f in enumerate(freq):
        count += f
        if count >= d // 2 and first is None:
            first = i
        if count >= (d // 2 + 1):
            second = i
            break

    # if it even, we need to calculate the median between two numbers
    return (first + second) / 2 if d % 2 == 0 else second

def activityNotifications(expenditure, d):
    notifications = 0
    # max value of number is 200
    freq = [0] * 201

    if d == 0 or d >= len(expenditure):
        return 0

    for i in range(d):
        freq[expenditure[i]] += 1

    for i in range(d, len(expenditure)):
        median = calculate_median(freq, d)

        if expenditure[i] >= 2 * median:
            notifications += 1

        freq[expenditure[i-d]] -= 1
        freq[expenditure[i]] += 1

    return notifications


# result = evaluate_test_case(activityNotifications, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(activityNotifications, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
