# Longest String Chain
# https://leetcode.com/problems/longest-string-chain/
# Accepted 2023-04-23 00:59 UTC · Python · 170 ms · 16.1 MB

class Solution:
    def longestStrChain(self, words) -> int:
        words = sorted(words, key=len)
        memo = defaultdict(int)
        for word in words:
            memo[word] = 1 + max(memo[word[:i] + word[i+1:]] for i in range(len(word)))
        return max(memo.values())
