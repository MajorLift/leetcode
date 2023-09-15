# Ransom Note
# https://leetcode.com/problems/ransom-note/
# Accepted 2023-09-15 05:49 UTC · Python · 84 ms (15.99%) · 16.5 MB (90.66%)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = [0] * 26
        for char in magazine:
            cnt[ord(char) - ord('a')] += 1
        for char in ransomNote:
            cnt[ord(char) - ord('a')] -= 1
            if cnt[ord(char) - ord('a')] < 0:
                return False
        return True
