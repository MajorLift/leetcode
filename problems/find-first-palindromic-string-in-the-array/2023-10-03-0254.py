# Find First Palindromic String in the Array
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
# Accepted 2023-10-03 02:54 UTC · Python · 93 ms (27.35%) · 16.3 MB (93.15%)

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(word: str) -> bool:
            return all(l == r for l, r in zip(word, reversed(word)))
        return (list(filter(isPalindrome, words)) or [""])[0]
