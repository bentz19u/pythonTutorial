from typing import Optional

from jovian.pythondsa import evaluate_test_case

from tests import test

from leetCode.listNode import ListNode

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


"""
Possible cases

1. generic case
"""


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    first_number = ''
    while l1:
        first_number = str(l1.val) + first_number
        l1 = l1.next

    second_number = ''
    while l2:
        second_number = str(l2.val) + second_number
        l2 = l2.next

    total = int(first_number) + int(second_number)
    result_list = list(str(total))
    result_list.reverse()

    dummy = ListNode()
    current = dummy

    for digit in result_list:
        current.next = ListNode(int(digit))
        current = current.next

    return dummy.next


result = evaluate_test_case(addTwoNumbers, test)
