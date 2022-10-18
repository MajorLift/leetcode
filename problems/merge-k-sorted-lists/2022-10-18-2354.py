# Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/
# Accepted 2022-10-18 23:54 UTC · Python · 243 ms · 18.2 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        setattr(ListNode, "__lt__", lambda self, other: self.val < other.val)
        head = ptr = ListNode()
        pq = [ll for ll in lists if ll]
        heapq.heapify(pq)
        while pq:
            curr = heapq.heappop(pq)
            ptr.next = ListNode(curr.val)
            ptr = ptr.next
            curr = curr.next
            if curr:
                heapq.heappush(pq, curr)
        return head.next
