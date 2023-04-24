# Height of Binary Tree After Subtree Removal Queries
# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/
# Accepted 2023-04-24 02:00 UTC · Python · 1174 ms · 90.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depths, heights = defaultdict(int), defaultdict(int)
        level = defaultdict(list)
        
        def dfs(node, depth):
            if not node:
                return -1
            depths[node.val] = depth
            height = max(
                dfs(node.left, depth + 1), 
                dfs(node.right, depth + 1),
            ) + 1
            heights[node.val] = height
            heappush(level[depth], (-height, node.val))
            return height
        dfs(root, 0)
        
        answer = []
        for query in queries:
            depth = depths[query]
            if len(level[depth]) == 1:
                answer.append(depth - 1)
            elif level[depth][0][1] == query:
                tmp = heappop(level[depth])
                answer.append(-level[depth][0][0] + depth)
                heappush(level[depth], tmp)
            else:
                answer.append(-level[depth][0][0] + depth)
        return answer
