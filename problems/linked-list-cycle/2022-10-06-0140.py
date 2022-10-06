# Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
# Accepted 2022-10-06 01:40 UTC · Python · 70 ms · 17.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head.next
        while True:
            if not fast or not fast.next:
                return False
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next
        return True
