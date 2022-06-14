# Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
# Accepted 2022-06-14 22:06 UTC · Python · 407 ms · 28.5 MB

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen = 0
        numset = set(nums)
        for num in numset:
            if num - 1 in numset:
                continue
            else:
                curr = num
                currlen = 1
                while curr + 1 in numset:
                    curr += 1
                    currlen += 1
                maxlen = max(maxlen, currlen)
        
        return maxlen
