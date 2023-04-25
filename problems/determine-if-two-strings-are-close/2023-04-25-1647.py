# Determine if Two Strings Are Close
# https://leetcode.com/problems/determine-if-two-strings-are-close/
# Accepted 2023-04-25 16:47 UTC · Python · 140 ms · 15.5 MB

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = map(Counter, (word1, word2))
        return set(cnt1.keys()) == set(cnt2.keys()) \
            and sorted(cnt1.values()) == sorted(cnt2.values())
