# Permutation in String
# https://leetcode.com/problems/permutation-in-string/
# Accepted 2023-02-01 23:00 UTC · Python · 39 ms · 14 MB

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        alphabet = {char: 0 for char in [chr(ord("a") + k) for k in range(26)]}
        cnt1, cnt2 = {**alphabet, **Counter(s1)}, {**alphabet, **Counter(s2[:n1])}
        if cnt1 == cnt2:
            return True
        for i in range(n1, n2):
            cnt2[s2[i]] += 1
            cnt2[s2[i - n1]] -= 1
            if cnt1 == cnt2:
                return True
        return False
