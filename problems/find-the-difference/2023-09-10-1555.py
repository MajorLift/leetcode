# Find the Difference
# https://leetcode.com/problems/find-the-difference/
# Accepted 2023-09-10 15:55 UTC · Python · 33 ms · 16.4 MB

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(reduce(lambda acc, curr: acc ^ ord(curr), s + t, 0))
