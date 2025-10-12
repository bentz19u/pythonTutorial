from leetCode.listNode import ListNode

test = {'input': {'list1': ListNode.from_list([1, 2, 4]), 'list2': ListNode.from_list([1, 3, 4])},
        'output': ListNode.from_list([1, 1, 2, 3, 4, 4])}

tests = [{'input': {'list1': ListNode.from_list([1, 2, 4]), 'list2': ListNode.from_list([1, 3, 4])},
          'output': ListNode.from_list([1, 1, 2, 3, 4, 4])},
         {'input': {'list1': ListNode.from_list([]), 'list2': ListNode.from_list([])},
          'output': ListNode.from_list([])},
         {'input': {'list1': ListNode.from_list([]), 'list2': ListNode.from_list([0])},
          'output': ListNode.from_list([0])}
         ]
