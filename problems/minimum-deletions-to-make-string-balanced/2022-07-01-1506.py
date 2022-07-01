# Minimum Deletions to Make String Balanced
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
# Accepted 2022-07-01 15:06 UTC · Python · 745 ms · 15.4 MB

class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = 0
        b_cnt = 0
        for char in s:
            if char == 'b':
                b_cnt += 1
            else:
                dp = min(b_cnt, dp + 1)
        return dp
