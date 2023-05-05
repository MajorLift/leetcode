# Maximum Number of Vowels in a Substring of Given Length
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Accepted 2023-05-05 04:49 UTC · Python · 180 ms · 18.1 MB

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        VOWELS = {'a', 'e', 'i', 'o', 'u'}
        prev = cnt = len([char for char in s[:k] if char in VOWELS])
        for r in range(k, len(s)):
            l = r - k + 1
            curr = prev \
                - (1 if s[l - 1] in VOWELS else 0) \
                + (1 if s[r] in VOWELS else 0)
            prev = curr
            cnt = max(cnt, curr)
        return cnt
