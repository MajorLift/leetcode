# Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# Accepted 2022-10-08 07:00 UTC · Python · 49 ms · 15.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
