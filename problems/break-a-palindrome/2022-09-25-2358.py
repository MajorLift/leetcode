# Break a Palindrome
# https://leetcode.com/problems/break-a-palindrome/
# Accepted 2022-09-25 23:58 UTC · Python · 60 ms · 13.8 MB

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n <= 1:
            return ""
        for i in range(n // 2):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i + 1:]
        return palindrome[:-1] + "b"
