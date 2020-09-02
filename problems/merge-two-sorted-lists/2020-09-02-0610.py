# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# Accepted 2020-09-02 06:10 UTC · Python · 40 ms · 14 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        small = l1
        large = l2
        if not small:
            return large
        if not large:
            return small
        if small.val > large.val:
            tmp = small
            small = large
            large = tmp
        head = small
        
        while small and large:
            if not small.next:
                small.next = large
                break
                
            if small.val > large.val:
                tmp = small
                small = large
                large = tmp
                
            if large.val <= small.next.val:
                tmp = large.next
                large.next = small.next
                small.next = large
                large = tmp
            small = small.next
                
        return head


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
