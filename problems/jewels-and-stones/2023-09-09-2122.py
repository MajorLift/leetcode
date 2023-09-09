# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/
# Accepted 2023-09-09 21:22 UTC · Python · 33 ms · 16.4 MB

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return ((jewels_set := set(jewels)), sum(stone in jewels_set for stone in stones))[1]
