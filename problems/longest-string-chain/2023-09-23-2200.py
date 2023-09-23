# Longest String Chain
# https://leetcode.com/problems/longest-string-chain/
# Accepted 2023-09-23 22:00 UTC · Python · 148 ms (59.8%) · 18.4 MB (21.48%)

class Solution:
    def longestStrChain(self, words) -> int:
        memo = defaultdict(int)
        for word in sorted(words, key=len):
            memo[word] = 1 + max(memo[word[:i] + word[i + 1:]] 
                                for i in range(len(word)))
        return max(memo.values())
