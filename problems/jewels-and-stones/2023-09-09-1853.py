# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/
# Accepted 2023-09-09 18:53 UTC · Python · 42 ms · 16.3 MB

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(Counter(stones)[jewel] for jewel in jewels)
