from typing import List, Optional

from jovian.pythondsa import evaluate_test_case

from tests import test

from leetCode.listNode import ListNode

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.


"""
Possible cases

1. generic case
"""


# ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 2, next: None}}}

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


result = evaluate_test_case(deleteDuplicates, test)
