test = {'input': {'s': "(([]){})"}, 'output': True}

tests = [{'input': {'s': "()"}, 'output': True},
         {'input': {'s': "()[]{}"}, 'output': True},
         {'input': {'s': "(]"}, 'output': False},
         {'input': {'s': "([])"}, 'output': True},
         {'input': {'s': "([)]"}, 'output': False},
         {'input': {'s': "["}, 'output': False},
         {'input': {'s': "(([]){})"}, 'output': True}
         ]
