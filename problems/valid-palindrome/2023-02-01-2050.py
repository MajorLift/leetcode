# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Accepted 2023-02-01 20:50 UTC · Python · 45 ms · 14.7 MB

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char for char in s if char.isalpha() or char.isnumeric()]
        return all(s[i].lower() == s[-(i + 1)].lower() for i in range(len(s) // 2))
