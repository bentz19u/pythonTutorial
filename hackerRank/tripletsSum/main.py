from jovian.pythondsa import evaluate_test_case

from tests import test


# Given 3 arrays a, b, c of different sizes, find the number of distinct triplets (p,q,r)
# where is an element of a,  satisfying the criteria p <= q and q >= r:
# For example, given a = [3,5,7], b=[3,6] and c = [4,6,9]
# we find four distinct triplets: (3,6,4),(3,6,6),(5,6,4),(5,6,6)

"""
Possible cases

1. generic case
2. no triplets
3. multiple same numbers
4. all same values
"""

# example of what kind of functions we are expecting (input and output)
def triplets_example(a, b, c):
    # correct result for test case 1
    return 8

def test_location(arr, mid, searched_number):
    # print(f"test_location mid {mid}, searched_number {searched_number}")
    if arr[mid] == searched_number:
        if mid - 1 >= 0 and arr[mid - 1] == searched_number:
            return 'left'
        else:
            return 'found'
    elif arr[mid] >= searched_number:
        return 'left'
    else:
        return 'right'

def find_closest_index(arr, searched_number):
    low, high = 0, len(arr) - 1
    closest_index = None

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= searched_number:
            closest_index = mid
            high = mid - 1  # Search left for closer match
        else:
            low = mid + 1  # Search right

    return closest_index

# test with using binary search, working but slow for large array
def triplets_old(a,b,c):
    result = 0

    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))

    # for each p, we will search the first index in b that validate the condition p <= q
    for p in a:
        # out of index
        if p > b[len(b) - 1]:
            continue

        b_idx_start = find_closest_index(b, p)
        # print(f"p {p}, b_idx_start {b_idx_start}")

        # we didn't find any numbers p <= q
        if b_idx_start is None:
            continue

        for q in range(b_idx_start, len(b)):
            # out of index
            if b[q] < c[0]:
                continue

            c_idx_start = find_closest_index(c, b[q])
            # print(f"q {q}, b[q] {b[q]}, c_idx_start {c_idx_start}")

            # we didn't find any numbers q >= r
            if c_idx_start is None:
                continue


            # we reach a point where there is triplets satisfying all conditions
            # print(f"adding {c_idx_start + 1}")
            result += c_idx_start + 1

    return result

# testing with pointers
def triplets_old(a,b,c):
    result = 0

    # removing the duplicates
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))

    print(a)
    print(b)
    print(c)

    # for each p, we will search the first index in b that validate the condition p <= q
    for first_num in a:
        # Start searching for b[q] such that p <= b[q]
        b_pointer = 0
        # print(f"b[b_pointer] {b[b_pointer]}, first_num {first_num}")
        while b_pointer < len(b) and b[b_pointer] < first_num:
            b_pointer += 1

        while b_pointer < len(b):
            c_pointer = 0
            # Move c_pointer backward to ensure c[c_pointer] <= b[b_pointer]
            print(f"c_pointer {c_pointer}, {c[c_pointer]}, {b[b_pointer]}")
            while c_pointer < len(c) and c[c_pointer] <= b[b_pointer]:
                print(f"first_num {first_num}, sec {b[b_pointer]}, third {c[c_pointer]}")
                c_pointer += 1

            # If c_pointer has valid values, count the remaining elements in 'c'
            if c_pointer < len(c) + 1:
                print(f"c_pointer {c_pointer+1}")
                result += c_pointer

            b_pointer += 1

    return result

# optimized version
def triplets(a, b, c):
    result = 0

    # removing the duplicates
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))

    # initialize pointers for arrays 'a' and 'c'
    a_pointer = 0
    c_pointer = 0

    for q in b:  # iterate through 'b' as the middle element
        # move a_pointer to count values in 'a' where p <= q
        while a_pointer < len(a) and a[a_pointer] <= q:
            a_pointer += 1

        # move c_pointer to count values in 'c' where r <= q
        while c_pointer < len(c) and c[c_pointer] <= q:
            c_pointer += 1

        # add the number of valid values from 'a' and 'c'
        result += a_pointer * c_pointer

    return result

result = evaluate_test_case(triplets, test)
print(result)