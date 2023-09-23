# Longest String Chain
# https://leetcode.com/problems/longest-string-chain/
# Accepted 2023-09-23 22:03 UTC · Python · 151 ms (58.85%) · 18.4 MB (23.58%)

class Solution:
    def longestStrChain(self, words) -> int:
        words.sort(key=len)
        memo = defaultdict(int)
        for word in words:
            memo[word] = 1 + max(memo[word[:i] + word[i + 1:]]
                                    for i in range(len(word)))
        return max(memo.values())
