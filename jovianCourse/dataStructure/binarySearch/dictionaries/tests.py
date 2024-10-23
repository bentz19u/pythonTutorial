tests = [{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'searched_number': 7}, 'output': 3},
         {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'searched_number': 1}, 'output': 6},
         {'input': {'cards': [4, 2, 1, -1], 'searched_number': 4}, 'output': 0},
         {'input': {'cards': [3, -1, -9, -127], 'searched_number': -127}, 'output': 3},
         {'input': {'cards': [6], 'searched_number': 6}, 'output': 0},
         {'input': {'cards': [9, 7, 5, 2, -9], 'searched_number': 4}, 'output': -1},
         {'input': {'cards': [], 'searched_number': 7}, 'output': -1},
         {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'searched_number': 3},
          'output': 7},
         {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
                    'searched_number': 6},
          'output': 2}]

large_test = {
    'input': {'cards': list(range(10000000, 0, -1)),
              'searched_number': 2},
    'output': 9999998
}

rotated_test = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}

rotated_tests = [
    {'input': {'nums': [24, 30, 35, 40, 45, 4, 6, 11]}, 'output': 5},
    {'input': {'nums': [4, 6, 11, 24, 30, 35, 40, 45]}, 'output': 0},
    {'input': {'nums': [45, 4, 6, 11, 24, 30, 35, 40]}, 'output': 1},
    {'input': {'nums': [6, 11, 24, 30, 35, 40, 45, 4]}, 'output': 7},
    {'input': {'nums': []}, 'output': -1},
    {'input': {'nums': [4]}, 'output': -1},
]
