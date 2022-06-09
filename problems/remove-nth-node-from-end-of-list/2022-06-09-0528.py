# Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Accepted 2022-06-09 05:28 UTC · Python · 90 ms · 13.8 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        fast, slow = head, head
        counter = 1
        
        while counter <= n:
            fast = fast.next
            counter += 1
            
        if fast is None and slow == head:
            return slow.next
        
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
                    
        skip_node = slow.next.next
        slow.next.next = None
        slow.next = skip_node
            
        return head
