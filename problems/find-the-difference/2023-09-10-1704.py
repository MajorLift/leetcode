# Find the Difference
# https://leetcode.com/problems/find-the-difference/
# Accepted 2023-09-10 17:04 UTC · Python · 39 ms · 16.4 MB

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(ord(e) for e in t) - sum(ord(e) for e in s))
