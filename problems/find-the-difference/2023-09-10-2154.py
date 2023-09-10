# Find the Difference
# https://leetcode.com/problems/find-the-difference/
# Accepted 2023-09-10 21:54 UTC · Python · 47 ms · 16.4 MB

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = map(lambda x: ''.join(sorted(x)), (s, t))
        for s_char, t_char in zip(s, t):
            if s_char != t_char: 
                return t_char
        return t[-1]
