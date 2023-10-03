# Find First Palindromic String in the Array
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
# Accepted 2023-10-03 02:55 UTC · Python · 100 ms (18.48%) · 16.3 MB (70.93%)

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(word: str) -> bool:
            n = len(word)
            return all(l == r for l, r in zip(word[:n // 2], reversed(word[n // 2:])))
        return (list(filter(isPalindrome, words)) or [""])[0]
