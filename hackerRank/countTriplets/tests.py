test = {'input': {'arr': [1, 4, 16, 64], 'r': 4}, 'output': 2}
# test = {'input': {'arr': [1, 5, 5, 25, 25, 125], 'r': 5}, 'output': 8}
# test = {'input': {'arr': [1 for _ in range(100)], 'r': 1}, 'output': 161700}

tests = [
    {
        'input': {'arr': [1, 4, 16, 64], 'r': 4},
        'output': 2
    },
    {
        'input': {'arr': [1, 2, 2, 4], 'r': 2},
        'output': 2
    },
    {
        'input': {'arr': [1, 3, 9, 9, 27, 81], 'r': 3},
        'output': 6
    },
    {
        'input': {'arr': [1, 5, 5, 25, 125], 'r': 5},
        'output': 4
    },
    {
        'input': {'arr': [1, 5, 5, 25, 25, 125], 'r': 5},
        'output': 8
    },
]
