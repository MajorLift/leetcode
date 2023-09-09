# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/
# Accepted 2023-09-09 18:43 UTC · Python · 42 ms · 16.2 MB

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in set(jewels) for stone in stones)
