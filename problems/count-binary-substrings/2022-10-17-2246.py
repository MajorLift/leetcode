# Count Binary Substrings
# https://leetcode.com/problems/count-binary-substrings/
# Accepted 2022-10-17 22:46 UTC · Python · 314 ms · 14.5 MB

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                count += 1
                k = 1
                while (i >= k and s[i - k] == s[i]) and (i + 1 + k < n and s[i + 1 + k] == s[i + 1]):
                    count += 1
                    k += 1
        return count
