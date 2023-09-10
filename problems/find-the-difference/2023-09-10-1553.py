# Find the Difference
# https://leetcode.com/problems/find-the-difference/
# Accepted 2023-09-10 15:53 UTC · Python · 39 ms · 16.5 MB

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n, m = map(len, (s, t))
        difference = 0
        for i in range(m):
            if i < n: difference -= ord(s[i])
            difference += ord(t[i])
        return chr(difference)
