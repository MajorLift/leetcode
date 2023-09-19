# Reverse String
# https://leetcode.com/problems/reverse-string/
# Accepted 2023-09-19 19:49 UTC · Python · 188 ms (82.19%) · 20.7 MB (48.83%)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[-(i + 1)] = s[-(i + 1)], s[i]
        return s
