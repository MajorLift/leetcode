# Maximum Number of Balloons
# https://leetcode.com/problems/maximum-number-of-balloons/
# Accepted 2023-08-29 21:43 UTC · Python · 48 ms · 16.3 MB

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_cnt, window_cnt = Counter("balloon"), Counter(text)
        return min(window_cnt[k] // balloon_cnt[k] for k in balloon_cnt)
