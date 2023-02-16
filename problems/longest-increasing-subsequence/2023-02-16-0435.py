# Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
# Accepted 2023-02-16 04:35 UTC · Python · 74 ms · 14.2 MB

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_seq = []
        for num in nums:
            idx = bisect_left(max_seq, num)
            if idx == len(max_seq):
                max_seq.append(num)
            else:
                max_seq[idx] = num
        return len(max_seq)
