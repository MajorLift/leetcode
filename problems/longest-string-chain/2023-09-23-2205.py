# Longest String Chain
# https://leetcode.com/problems/longest-string-chain/
# Accepted 2023-09-23 22:05 UTC · Python · 154 ms (57.62%) · 18.2 MB (25.62%)

class Solution:
    def longestStrChain(self, words) -> int:
        words.sort(key=len)
        memo = defaultdict(int)
        for word in words:
            memo[word] = 1 + max(
                memo[word[:i] + word[i + 1:]]
                for i in range(len(word)))
        return max(memo.values())
