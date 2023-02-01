# Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
# Accepted 2023-02-01 04:32 UTC · Python · 306 ms · 28.9 MB

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        ans = 0
        for num in hashset:
            if num - 1 not in hashset:
                curr = num
                local = 0
                while curr in hashset:
                    curr += 1
                    local += 1
                ans = max(ans, local)
        return ans
