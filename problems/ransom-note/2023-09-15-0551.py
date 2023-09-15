# Ransom Note
# https://leetcode.com/problems/ransom-note/
# Accepted 2023-09-15 05:51 UTC · Python · 70 ms (42.86%) · 16.6 MB (61.5%)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = [0] * 26
        for char in magazine:
            cnt[ord(char) - ord('a')] += 1
        for char in ransomNote:
            curr = ord(char) - ord('a')
            cnt[curr] -= 1
            if cnt[curr] < 0:
                return False
        return True
