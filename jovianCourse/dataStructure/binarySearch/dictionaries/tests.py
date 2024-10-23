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
 'input': {'cards': list(range(10000000, 0 , -1)),
           'searched_number': 2},
 'output': 9999998
}