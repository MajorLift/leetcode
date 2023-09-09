# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/
# Accepted 2023-09-09 22:06 UTC · Python · 42 ms · 16.2 MB

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in (jewels_set := set(jewels)) for stone in stones)
