# Find the Difference
# https://leetcode.com/problems/find-the-difference/
# Accepted 2023-09-10 15:42 UTC · Python · 39 ms · 16.3 MB

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list((Counter(t) - Counter(s)).keys()).pop()
