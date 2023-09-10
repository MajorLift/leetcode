# Find the Difference
# https://leetcode.com/problems/find-the-difference/
# Accepted 2023-09-10 22:00 UTC · Python · 52 ms · 16.4 MB

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return [t_char for s_char, t_char in zip(*map(sorted, (s + "!", t))) if s_char != t_char].pop()
