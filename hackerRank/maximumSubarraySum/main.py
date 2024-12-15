from jovian.pythondsa import evaluate_test_case

from tests import test

import bisect


# We define the following:
# A subarray of array a of length n is a contiguous segment from a[i] through a[j] where 0 <= i <= j < n.
# The sum of an array is the sum of its elements.
# Given an n element array of integers, a, and an integer, m,
# determine the maximum value of the sum of any of its subarrays modulo m.


#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
# a = [3,3,9,9,5]
# m = 7
# return 6

def maximumSumExample(a, m):
    return 6


def maximumSumOld(a, m):
    def recursive(a, m):
        if len(a) <= 1:
            return a[0], a[0] % m

        mid = len(a) // 2

        left = a[:mid]
        right = a[mid:]

        left_sum_modulo, left_result = recursive(left, m)
        right_sum_modulo, right_result = recursive(right, m)

        sum = left_sum_modulo + right_sum_modulo
        mod = sum % m

        mod = left_result if left_result > mod else mod
        mod = right_result if right_result > mod else mod

        return sum, mod

    # normal binary search
    sum, mod = recursive(a, m)

    return mod


def maximumSum(a, m):
    prefix = 0
    max_mod = 0
    prefix_set = [0]  # Initialize with 0 to handle full array cases

    for num in a:
        # Update the prefix sum
        prefix = (prefix + num) % m

        # Use binary search to find the smallest prefix larger than the current prefix
        idx = bisect.bisect_right(prefix_set, prefix)
        if idx < len(prefix_set):
            # Check the subarray sum modulo m
            max_mod = max(max_mod, (prefix - prefix_set[idx] + m) % m)

        # Update the max_mod for the current prefix
        max_mod = max(max_mod, prefix)

        # Insert the current prefix in sorted order
        bisect.insort(prefix_set, prefix)

    return max_mod


result = evaluate_test_case(maximumSum, test)
