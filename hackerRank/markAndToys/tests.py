test = {'input': {'prices': [1, 12, 5, 111, 200, 1000, 10], 'k': 50}, 'output': 4}

tests = [{'input': {'prices': [1, 12, 5, 111, 200, 1000, 10], 'k': 50}, 'output': 4},
         {'input': {'prices': [10, 12, 50, 111, 200, 1000, 15], 'k': 5}, 'output': 0},
         {'input': {'prices': [1, 12, 5, 111, 200, 1000, 10], 'k': 50000}, 'output': 7},
         {'input': {'prices': [], 'k': 50}, 'output': 0},
         ]