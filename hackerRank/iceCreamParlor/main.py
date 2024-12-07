# Each time Sunny and Johnny take a trip to the Ice Cream Parlor,
# they pool their money to buy ice cream. On any given day,
# the parlor offers a line of flavors. Each flavor has a cost associated with it.
# Given the value of money and the cost of each flavor for trips to the Ice Cream Parlor,
# help Sunny and Johnny choose two distinct flavors such that they spend
# their entire pool of money during each visit.
# ID numbers are the 1- based index number associated with a cost.
# For each trip to the parlor, print the ID numbers for
# the two types of ice cream that Sunny and Johnny purchase as
# two space-separated integers on a new line.
# You must print the smaller ID first and the larger ID second.

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

# cost = [1, 4, 5, 3, 2]
# money = 4
# The first time, they pool together dollars money = 4. There are five flavors available
# that day and flavors 1 and 4 have a total cost of  1 + 3 = 4.
def whatFlavorsExample(cost, money):
    print('1 4')

def whatFlavors(cost, money):
    number_by_index = {}

    # first we map the index where the numbers are
    for i, value in enumerate(cost):
        if value not in number_by_index:
            number_by_index[value] = []
        number_by_index[value].append(i)

    # when for each value, we will check if we match a pair
    for i, value in enumerate(cost):
        searched_number = money - value
        if searched_number in number_by_index:
            for j in number_by_index[searched_number]:
                if i != j:
                    print(f"{i + 1} {j + 1}")
                    return

def whatFlavorsOptimized(cost, money):
    number_by_index = {}

    for i, value in enumerate(cost):
        searched_number = money - value
        if searched_number in number_by_index:
            # Found a pair
            print(f"{number_by_index[searched_number] + 1} {i + 1}")
            return
        # Store the current number and its index
        number_by_index[value] = i


whatFlavorsOptimized([4,3,2,5,7], 8)