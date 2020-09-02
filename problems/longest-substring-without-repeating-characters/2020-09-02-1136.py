# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Accepted 2020-09-02 11:36 UTC · Python · 56 ms · 14.1 MB

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxlen = 0
        sub = ""

        while right < len(s):
            if s[right] not in sub:
                sub += s[right]
                if len(sub) > maxlen:
                    maxlen = len(sub)
                right += 1
            else:
                left += 1
                sub = s[left:right]
                
        return maxlen
