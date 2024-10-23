tests = []

# searched_number occurs in the middle
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'searched_number': 1
    },
    'output': 6
})

# searched_number is the first element in cards
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'searched_number': 4
    },
    'output': 0
})

# searched_number is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'searched_number': -127
    },
    'output': 3
})

# cards contains just one element, searched_number
tests.append({
    'input': {
        'cards': [6],
        'searched_number': 6
    },
    'output': 0
})

# cards does not contain searched_number
# we assume it returns -1 in this case
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'searched_number': 4
    },
    'output': -1
})

# cards is empty
tests.append({
    'input': {
        'cards': [],
        'searched_number': 7
    },
    'output': -1
})

# searched_number can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'searched_number': 3
    },
    'output': 7
})