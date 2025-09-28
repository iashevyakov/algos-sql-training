# https://leetcode.com/problems/merge-two-sorted-lists/description/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = ListNode()
        zero_elem = cur_node
        while list1 and list2:
            if list1.val < list2.val:
                cur_node.next = list1
                list1, cur_node = list1.next, list1
            else:
                cur_node.next = list2
                list2, cur_node = list2.next, list2

        if list1 or list2:
            cur_node.next = list1 if list1 else list2

        return zero_elem.next