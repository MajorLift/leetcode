# Minimum Changes To Make Alternating Binary String
# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
# Accepted 2023-08-31 05:13 UTC · Python · 52 ms · 16.4 MB

class Solution:
    def minOperations(self, s: str) -> int:
        diff = sum(e != "01"[i % 2] for i,e in enumerate(s))
        return min(diff, len(s) - diff)
