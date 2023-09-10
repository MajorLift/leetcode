# Find the Difference
# https://leetcode.com/problems/find-the-difference/
# Accepted 2023-09-10 18:25 UTC · Python · 45 ms · 16.3 MB

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = map(lambda x: ''.join(sorted(x)), (s, t))
        i = j = 0
        while i < len(s) and j < len(t) and s[i] == t[j]:
            i += 1
            j += 1
        return t[j]
