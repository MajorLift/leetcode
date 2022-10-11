# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# Accepted 2022-10-11 17:06 UTC · Python · 83 ms · 14 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)
        curr, l1, l2 = prehead, list1, list2
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return prehead.next
