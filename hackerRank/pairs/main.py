from jovian.pythondsa import evaluate_test_case

from tests import test


# Given an array of integers and a target value,
# determine the number of pairs of array elements that have a difference equal to the target value.

# arr = [1, 5, 3, 4, 2]
# k = 2
# There are 3 pairs of integers in the set with a difference of 2: [5,3], [4,2] and [3,1]. .
def pairs_example(k, arr):
    return 3


def pairs(k, arr):
    sorted_arr = sorted(arr)
    length = len(sorted_arr) - 1
    count_pairs = 0

    idx1, idx2 = 0, 1
    while idx1 <= length and idx2 <= length:
        diff = sorted_arr[idx2] - sorted_arr[idx1]
        if diff == k:
            count_pairs += 1
            idx2 += 1
        elif diff > k:
            idx1 += 1
        else:
            idx2 += 1

    return count_pairs


result = evaluate_test_case(pairs, test)
print(result)
