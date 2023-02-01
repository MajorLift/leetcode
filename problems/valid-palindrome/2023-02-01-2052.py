# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Accepted 2023-02-01 20:52 UTC · Python · 48 ms · 19.2 MB

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalpha() or char.isnumeric()]
        return all(s[i] == s[-(i + 1)] for i in range(len(s) // 2))
