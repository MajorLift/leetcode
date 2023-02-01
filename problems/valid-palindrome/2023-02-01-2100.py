# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Accepted 2023-02-01 21:00 UTC · Python · 48 ms · 14.8 MB

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.findall('[a-zA-Z0-9]', s)
        return all(s[i].lower() == s[-(i + 1)].lower() for i in range(len(s) // 2))
