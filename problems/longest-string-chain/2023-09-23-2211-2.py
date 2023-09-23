# Longest String Chain
# https://leetcode.com/problems/longest-string-chain/
# Accepted 2023-09-23 22:11 UTC · Python · 165 ms (53.48%) · 43 MB (5.01%)

class Solution:
    def longestStrChain(self, words) -> int:
        words.sort(key=len)
        word_set = set(words)
        @cache
        def dp(word):
            if word not in word_set:
                return 0
            return 1 + max(dp(word[:i] + word[i + 1:]) 
                            for i in range(len(word)))
        return max(dp(word) for word in words)
