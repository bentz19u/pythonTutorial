from jovian.pythondsa import evaluate_test_case

from dictionnaries.tests import test, tests


# given n elements, each of which has a weight and a profit, determine the maximum profit that can be
# obtained by selecting a subset of the elements weighing no more than w.

def get_max_profit(capacity, weights, profits, idx=0):
    if len(weights) <= idx:
        return 0

    if weights[idx] > capacity:
        return get_max_profit(capacity, weights, profits, idx + 1)

    # first option is, we do not take this profit/weight, and we continue to check the rest
    option1 = get_max_profit(capacity, weights, profits, idx + 1)

    # second option is, we keep it and continue to check the rest
    # we also remove the weight from the capacity
    option2 = profits[idx] + get_max_profit(capacity - weights[idx], weights, profits, idx + 1)

    return max(option1, option2)

def get_max_profit_dynamic_prog(capacity, weights, profits):
    weight_len = len(weights)
    results = [[0 for _ in range(capacity+1)] for _ in range(weight_len + 1)]

    # we create and fill a 2-dimensional array that will give us a list of max profits
    # per weight/profit and for each capacity
    for weight_idx in range(weight_len):
        for cap in range(capacity+1):
            if weights[weight_idx] > cap:
                results[weight_idx + 1][cap] = results[weight_idx][cap]
            else:
                results[weight_idx + 1][cap] = max(results[weight_idx][cap], profits[weight_idx] + results[weight_idx][cap - weights[weight_idx]])

    # the max profit will be the last element of the array
    return results[-1][-1]


# result = evaluate_test_case(get_max_profit, test)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(get_max_profit_dynamic_prog, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")