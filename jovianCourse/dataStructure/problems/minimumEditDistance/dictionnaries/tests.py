test = {
    'input': {'str1': 'intention',
              'str2': 'execution'},
    'output': 5
}

tests = [
    {'input': {'str1': 'intention', 'str2': 'execution'}, 'output': 5},
    {'input': {'str1': 'intention', 'str2': 'intention'}, 'output': 0},
    {'input': {'str1': 'intention', 'str2': 'composure'}, 'output': 9},
    {'input': {'str1': 'intention', 'str2': 'intent'}, 'output': 3},
    {'input': {'str1': 'intention', 'str2': ''}, 'output': 9},
    {'input': {'str1': 'intention', 'str2': 'intentional'}, 'output': 2},
    {'input': {'str1': 'intent', 'str2': 'intention'}, 'output': 3},
    {'input': {'str1': 'intention', 'str2': 'composure'}, 'output': 9},
]
