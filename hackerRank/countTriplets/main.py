from jovian.pythondsa import evaluate_test_case

from dictionnaries.tests import test, tests


# You are given an array, and you need to find number of triplets of indices (i,j,k)
# such that the elements at those indices are in geometric progression
# for a given common ratio r and i and i < j < k.
# https://en.wikipedia.org/wiki/Geometric_progression

# example
# arr = [1,4,16,64], r = 4
# There are [1,4,16] and [4,16,64] at indices (0,1,2) and (1,2,3) . Return 2.

# example of what kind of functions we are expecting (input and output)
def count_triplets_example(arr, r):
    # correct result for test case 1
    return 2


"""
Possible cases

1. generic case
2. no triplets
3. multiple same numbers
4. all same values
"""

# time complexity of o(n3), brute force example
def count_triplets_brute_force(arr, r, idx1=0, idx2=1, idx3=2):
    result = 0
    # first, we check if the currents indexes match a triplets
    if arr[idx1] * r == arr[idx2] and arr[idx2] * r == arr[idx3]:
        result += 1

    # we will first call recursively by increasing the last idx3
    if idx3 < len(arr) - 1:
        result += count_triplets_brute_force(arr, r, idx1, idx2, idx3 + 1)
        # then we increase idx2, idx3 is reset to the next index from idx2
    elif idx2 < len(arr) - 2:
        result += count_triplets_brute_force(arr, r, idx1, idx2 + 1, idx2 + 2)
        # then we increase idx1, and reset the others
    elif idx1 < len(arr) - 3:
        result += count_triplets_brute_force(arr, r, idx1 + 1, idx1 + 2, idx1 + 3)

    return result

# result = evaluate_test_case(count_triplets_brute_force, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(count_triplets_brute_force, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")
