from jovian.pythondsa import evaluate_test_case

from dictionnaries.tests import test, tests


# Write a function to find the length of the longest common subsequence between two sequences.
# E.g. Given the strings "serendipitous" and "precipitation", the longest common subsequence is "reipito" and its length is 7.
# A "sequence" is a group of items with a deterministic ordering. Lists, tuples and ranges are some common sequence types in Python.
# A "subsequence" is a sequence obtained by deleting zero or more elements from another sequence.
# For example, "edpt" is a subsequence of "serendipitous".

# check subsequence_example img for an example

# the idea is to test each first char of each sequence
# if the char match, we increase the index of both array and check the new sub strings
# if they don't, we will test twice the two sub strings, one for seq1 and one for seq2
# each recursive will only test one char of each sequence at a time
def length_common_subsequence(seq1, seq2, seq1_index=0, seq2_index=0, match_found=0):
    if seq1_index >= len(seq1) or seq2_index >= len(seq2):
        return match_found

    if seq1[seq1_index] == seq2[seq2_index]:
        match_found += 1
        match_found = length_common_subsequence(seq1, seq2, seq1_index + 1, seq2_index + 1, match_found)
    else:
        first_match_found = length_common_subsequence(seq1, seq2, seq1_index + 1, seq2_index, match_found)
        second_match_found = length_common_subsequence(seq1, seq2, seq1_index, seq2_index + 1, match_found)
        match_found = max(first_match_found, second_match_found)

    return match_found


is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(length_common_subsequence, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")

# time complexity of O(2^m+n)