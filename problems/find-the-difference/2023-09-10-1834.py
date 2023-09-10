# Find the Difference
# https://leetcode.com/problems/find-the-difference/
# Accepted 2023-09-10 18:34 UTC · Python · 44 ms · 16.4 MB

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = map(lambda x: ''.join(sorted(x)), (s, t))
        for i in range(len(t)):
            if t[i] != (s[i] if i < len(s) else None): 
                return t[i]
