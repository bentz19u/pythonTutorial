test = {'input': {'expenditure': [2, 3, 4, 2, 3, 6, 8, 4, 5], 'd': 5}, 'output': 2}

"""
Possible clases

1. generic case with notifications
2. generic case with no notification
3. d bigger than the number of cases
4. d at 0?
5. d at 1?
6. very long expenditure and d

"""

tests = [
    {'input': {'expenditure': [2, 3, 4, 2, 3, 6, 8, 4, 5], 'd': 5}, 'output': 2},
    {'input': {'expenditure': [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3], 'd': 5}, 'output': 0},
    {'input': {'expenditure': [2, 3, 4, 2, 3, 6, 8, 4, 5], 'd': 20}, 'output': 0},
    {'input': {'expenditure': [2, 3, 4, 2, 3, 6, 8, 4, 5], 'd': 0}, 'output': 0},
    {'input': {'expenditure': [2, 3, 4, 2, 3, 6, 8, 4, 5], 'd': 1}, 'output': 1},
]
