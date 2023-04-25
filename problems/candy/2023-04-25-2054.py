# Candy
# https://leetcode.com/problems/candy/
# Accepted 2023-04-25 20:54 UTC · Python · 175 ms · 16.7 MB

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        memo = [1] * n
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                memo[i] = max(memo[i], memo[i - 1] + 1)
        for i in range(n - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                memo[i] = max(memo[i], memo[i + 1] + 1)
        return sum(memo)
