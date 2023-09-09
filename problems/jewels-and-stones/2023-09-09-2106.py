# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/
# Accepted 2023-09-09 21:06 UTC · Python · 38 ms · 16.4 MB

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in jewels_set for stone in stones if (jewels_set := set(jewels)))
