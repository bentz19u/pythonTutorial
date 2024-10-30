test = {
    'input': {'nums': [1, 7, 4, 2, 1, 3, 11, 5],
              'target': 10},
    'output': [2, 5]
}

tests = [
    {'input': {'nums': [1, 7, 4, 2, 1, 3, 11, 5], 'target': 10}, 'output': [2, 5]},
    {'input': {'nums': [4, 2, 1, 3, 1, 7, 11, 5], 'target': 10}, 'output': [0, 3]},
    {'input': {'nums': [1, 7, 11, 5, 4, 2, 1, 3], 'target': 10}, 'output': [4, 7]},
    {'input': {'nums': [1, 7, 11, 5, 3, 8, 1, 3], 'target': 10}, 'output': [None, None]},
    {'input': {'nums': [4, 2, 1, 3, 4, 2, 1, 3, 4, 2, 1, 3], 'target': 10}, 'output': [0, 3]},
    {'input': {'nums': [], 'target': 10}, 'output': [None, None]},
    {'input': {'nums': [1, 7, 11, 5, 3, 10, 1, 3], 'target': 10}, 'output': [5, 5]},
]
