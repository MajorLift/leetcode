# Subsets
# https://leetcode.com/problems/subsets/
# Accepted 2022-09-14 21:44 UTC · Python · 63 ms · 14.2 MB

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            queue = deque(output)
            while queue:
                curr = queue.popleft().copy()
                curr.append(num)
                output.append(curr)
        return output
