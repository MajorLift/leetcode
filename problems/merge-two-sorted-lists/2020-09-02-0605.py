# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# Accepted 2020-09-02 06:05 UTC · Python · 68 ms · 13.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        small = l1
        large = l2
        if l1.val > l2.val:
            small = l2
            large = l1
        head = small
        
        while small and large:
            if small.val > large.val:
                tmp = small
                small = large
                large = tmp
                
            if small.next:                   
                if large.val <= small.next.val:
                    tmp = large.next
                    large.next = small.next
                    small.next = large
                    large = tmp
                    small = small.next
                else:
                    # if large.next and \
                    # small.next.val > large.next.val:
                    #     large = large.next
                    small = small.next                    

            else:
                small.next = large
                break
                
        return head


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
