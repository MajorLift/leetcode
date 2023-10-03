# Find First Palindromic String in the Array
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
# Accepted 2023-10-03 02:51 UTC · Python · 102 ms (15.54%) · 16.3 MB (93.15%)

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return (list(filter(self.isPalindrome, words)) or [""])[0]
    
    def isPalindrome(self, word: str) -> bool:
        return all(l == r for l, r in zip(word, reversed(word)))
