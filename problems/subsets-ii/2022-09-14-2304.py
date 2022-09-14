# Subsets II
# https://leetcode.com/problems/subsets-ii/
# Accepted 2022-09-14 23:04 UTC · Python · 77 ms · 14.2 MB

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        subsets = [[]]
        num_prev_subsets = 0
        for i, num in enumerate(nums_sorted):
            start_idx = num_prev_subsets if i > 0 and num == nums_sorted[i - 1] else 0
            num_prev_subsets = len(subsets)
            queue = deque(subsets[start_idx:])
            while queue:
                curr = queue.popleft().copy()
                curr.append(num)
                subsets.append(curr)
        return subsets
