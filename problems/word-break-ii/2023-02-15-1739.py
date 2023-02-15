# Word Break II
# https://leetcode.com/problems/word-break-ii/
# Accepted 2023-02-15 17:39 UTC · Python · 34 ms · 13.8 MB

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n, wordSet = len(s), set(wordDict)
        memo = [[] for _ in range(n + 1)]
        for r in range(1, n + 1):
            for l in range(r):
                if s[l:r] in wordSet:
                    if l == 0:
                        memo[r] += [s[l:r]]
                    else:
                        memo[r] += [fragment + " " + s[l:r] for fragment in memo[l]]
        return memo[-1]
