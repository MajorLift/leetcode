# Ransom Note
# https://leetcode.com/problems/ransom-note/
# Accepted 2023-09-15 17:24 UTC · Python · 105 ms (6.49%) · 16.5 MB (61.5%)

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
            if target[i] == source[j]:
                i += 1
            j += 1
