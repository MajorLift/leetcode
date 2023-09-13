# Candy
# https://leetcode.com/problems/candy/
# Accepted 2023-09-13 02:29 UTC · Python · 154 ms (38.85%) · 19.2 MB (91.55%)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        memo = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                memo[i] = max(memo[i], memo[i - 1] + 1)
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                memo[i] = max(memo[i], memo[i + 1] + 1)
        return sum(memo)
