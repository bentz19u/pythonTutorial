from jovian.pythondsa import evaluate_test_case

from dictionnaries.tests import test, tests

# Determine the minimum cost to provide library access to all citizens of HackerLand.
# There are n cities numbered from 1 to n.
# Currently, there are no libraries and the cities are not connected.
# Bidirectional roads may be built between any city pair listed in cities.
# A citizen has access to a library if:
# Their city contains a library.
# They can travel by road from their city to a city containing a library.

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

"""
Possible cases

1. generic case, lib cost higher than road
2. generic case, lib cost lower than road
3. empty city list
4. cities cannot be connected, cost is one library in every city
"""

def make_adjacency_list(n, edges):
    result = [[] for _ in range(n)]
    for n1, n2 in edges:
        result[n1 - 1].append(n2 - 1)
        result[n2 - 1].append(n1 - 1)
    return result

# didnt work in case of the cities not being ordered by index
def roadsAndLibraries_old(n, c_lib, c_road, cities):
    adjacency_list = make_adjacency_list(n, cities)
    print(adjacency_list)
    visited = [False] * n
    used_points = 0
    idx = 0

    while idx < n:
        print(idx)
        if not visited[idx]:
            print(idx, 'not visited + 3 library')
            visited[idx] = True
            # never visited, it doesn't have a library
            used_points += c_lib

        # edge case when library are so cheap we can build them everywhere
        if c_lib < c_road:
            idx += 1
            continue

        for target_idx in adjacency_list[idx]:
            if not visited[target_idx]:
                print(idx, target_idx, 'not visited + 1 road')
                visited[target_idx] = True
                used_points += c_road

        idx += 1

    return used_points

def roadsAndLibraries(n, c_lib, c_road, cities):
    adjacency_list = make_adjacency_list(n, cities)
    visited = [False] * n
    used_points = 0
    idx = 0

    def count_road_recursive(idx):
        used_points = 0
        for target_idx in adjacency_list[idx]:
            if visited[target_idx]:
                continue

            visited[target_idx] = True
            # we add a road
            used_points += c_road
            used_points += count_road_recursive(target_idx)

        return used_points

    while idx < n:
        if not visited[idx]:
            visited[idx] = True
            # never visited, it doesn't have a library
            used_points += c_lib

        # edge case when library are so cheap we can build them everywhere
        if c_lib < c_road:
            idx += 1
            continue

        used_points += count_road_recursive(idx)

        idx += 1

    return used_points


# result = evaluate_test_case(roadsAndLibraries, test)
# print(result)

is_all_tests_succeed = True
time_to_process = 0

for test in tests:
    result = evaluate_test_case(roadsAndLibrariesV2, test)
    time_to_process += result[2]

    # index 1 has a boolean if the test worked or not
    if not result[1]:
        is_all_tests_succeed = False

print(f"ALL TESTS SUCCEED? {is_all_tests_succeed}, time to process {time_to_process}")