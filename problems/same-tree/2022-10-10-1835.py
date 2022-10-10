# Same Tree
# https://leetcode.com/problems/same-tree/
# Accepted 2022-10-10 18:35 UTC · Python · 64 ms · 13.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        queue_p, queue_q = deque([p]), deque([q])
        while queue_p and queue_q:
            curr_p, curr_q = queue_p.popleft(), queue_q.popleft()
            if curr_p and curr_q:
                if curr_p.val != curr_q.val:
                    return False
                queue_p.append(curr_p.left)
                queue_p.append(curr_p.right)
                queue_q.append(curr_q.left)
                queue_q.append(curr_q.right)
            elif not curr_p and not curr_q:
                continue
            else:
                return False
        return True
