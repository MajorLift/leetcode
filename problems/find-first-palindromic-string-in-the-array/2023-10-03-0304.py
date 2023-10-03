# Find First Palindromic String in the Array
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
# Accepted 2023-10-03 03:04 UTC · Python · 91 ms (29.88%) · 16.4 MB (70.93%)

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return next(filter(
                        lambda word: all(
                            l == r 
                            for l, r in zip(
                                word[:len(word) // 2 + 1], 
                                word[len(word) - 1:len(word) // 2 - 1:-1]
                            )), 
                        words),
                    "")
