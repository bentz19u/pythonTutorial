test = {'input': {'nums': [4, 2, 6, 3, 4, 6, 2, 1]}, 'output': 16}
# test = {'input': {'nums': [2, 3, 4, 6, 1, 2, 4, 6]}, 'output': 8}

tests = [{'input': {'nums': [4, 2, 6, 3, 4, 6, 2, 1]}, 'output': 16},
         {'input': {'nums': [2, 4, 1]}, 'output': 2},
         {'input': {'nums': [3, 5, 6, 8, 9, 10, 99]}, 'output': 0},
         {'input': {'nums': [4,3,2,1]}, 'output': 6},
         {'input': {'nums': []}, 'output': 0},
         ]

large_test = {
    'input': {'nums': list(range(10000, 0, -1))},
    'output': 10000
}

"""
Possible cases

1. generic case, there is a few inversions
2. no inversions, it's already sorted
3. the list is completely inversed
3. empty list
4. very long list
"""
#
# [4, 2, 6, 3, 4, 6, 2, 1]
#
# 2 4 6 3 4 6 2 1
# 2 4 3 6 4 6 2 1
# 2 3 4 6 4 6 2 1
# 2 3 4 4 6 6 2 1
# 2 3 4 4 6 2 6 1
# 2 3 4 4 2 6 6 1
# 2 3 4 2 4 6 6 1
# 2 3 2 4 4 6 6 1
# 2 2 3 4 4 6 6 1
# 2 2 3 4 4 6 1 6
# 2 2 3 4 4 1 6 6
# 2 2 3 4 1 4 6 6
# 2 2 3 1 4 4 6 6
# 2 2 1 3 4 4 6 6
# 2 1 2 3 4 4 6 6
# 1 2 2 3 4 4 6 6

# start [4] [2] 0
# end [2, 4] 1
# start [6] [3] 0
# end [3, 6] 1
# start [2, 4] [3, 6] 2
# end [2, 3, 4, 6] 3
# start [4] [6] 0
# end [4, 6] 0
# start [2] [1] 0
# end [1, 2] 1
# start [4, 6] [1, 2] 1
# end [1, 2, 4, 6] 5
# start [2, 3, 4, 6] [1, 2, 4, 6] 8
# end [1, 2, 2, 3, 4, 4, 6, 6] 12
#
# 2 4 3 6 4 6 1 2 === 3
# 2 3 4 6 1 3 4 6 = 5 + 3
# 1 2 3 4 6 3 4 6 = 4 + 8