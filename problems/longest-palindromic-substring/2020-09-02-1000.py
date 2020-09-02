# Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# Accepted 2020-09-02 10:00 UTC · Python · 756 ms · 13.6 MB

class Solution:
    def longestPalindrome(self, s: str) -> str:
        resleft = 0
        resright = 0
        reslen = 0
        
        for curr in range(1,len(s)):
            left = curr
            right = curr
            if s[curr] == s[curr-1]:
                left = curr-1
                while right < len(s) and s[right] == s[left]:
                    right += 1
                right -= 1
                
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                else:
                    if right - left + 1 > reslen:
                        resleft = left
                        resright = right
                        reslen = right - left + 1
                    left -= 1
                    right += 1
        
        return s[resleft:resright+1]
