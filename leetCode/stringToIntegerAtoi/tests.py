test = {'input': {'s': '42'}, 'output': 42}

tests = [{'input': {'s': '42'}, 'output': 42},
         {'input': {'s': ' -042'}, 'output': -42},
         {'input': {'s': '1337c0d3'}, 'output': 1337},
         {'input': {'s': '0-1'}, 'output': 0},
         {'input': {'s': 'words and 987'}, 'output': 0}
         ]
