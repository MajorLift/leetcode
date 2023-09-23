# Longest String Chain
# https://leetcode.com/problems/longest-string-chain/
# Accepted 2023-09-23 22:12 UTC · Python · 157 ms (56.31%) · 43 MB (5.01%)

class Solution:
    def longestStrChain(self, words) -> int:
        word_set = set(words)
        @cache
        def dp(word):
            if word not in word_set:
                return 0
            return 1 + max(dp(word[:i] + word[i + 1:]) 
                            for i in range(len(word)))
        return max(dp(word) for word in sorted(words, key=len))
