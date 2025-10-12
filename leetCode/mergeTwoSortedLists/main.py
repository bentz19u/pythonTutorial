from typing import Optional

from jovian.pythondsa import evaluate_test_case

from leetCode.listNode import ListNode
from tests import test, tests

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

"""
Possible cases

1. generic case
2. both lists are empty
3. one list is empty
"""


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 or list2

    return dummy.next


result = evaluate_test_case(mergeTwoLists, test)
