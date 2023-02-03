# Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/
# Accepted 2023-02-03 07:12 UTC · Python · 35 ms · 13.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = [root.val]
        queue = deque([root])
        while queue:
            next_level = []
            while queue:
                curr = queue.popleft()
                if curr.left:
                    next_level.append(curr.left)
                if curr.right:
                    next_level.append(curr.right)
            if not next_level:
                break
            output.append(next_level[-1].val)
            queue += next_level
        return output
