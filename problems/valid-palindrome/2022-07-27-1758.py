# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Accepted 2022-07-27 17:58 UTC · Python · 102 ms · 14.6 MB

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alpha = ""
        for char in s:
            if char.isalnum():
                s_alpha += char.lower()
        print(s_alpha)
        return all(s_alpha[i] == s_alpha[-(i + 1)] for i in range(len(s_alpha) // 2))
