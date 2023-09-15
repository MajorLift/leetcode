# Ransom Note
# https://leetcode.com/problems/ransom-note/
# Accepted 2023-09-15 06:09 UTC · Python · 106 ms (6.28%) · 16.7 MB (9.07%)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        target, source = map(sorted, (ransomNote, magazine))
        m, n = map(len, (target, source))
        i = j = 0
        while True:
            if i == m:
                return True
            if j == n:
                return False
            while i < m and j < n and target[i] == source[j]:
                i += 1
                j += 1
            while i < m and j < n and target[i] != source[j]:
                j += 1
