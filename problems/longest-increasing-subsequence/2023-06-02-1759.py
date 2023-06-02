# Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
# Accepted 2023-06-02 17:59 UTC · Python · 90 ms · 16.8 MB

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subseq = [nums[0]]
        for num in nums[1:]:
            if num > subseq[-1]:
                subseq.append(num)
            else:
                subseq[bisect_left(subseq, num)] = num
        return len(subseq)
