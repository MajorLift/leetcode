# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/
# Accepted 2023-09-09 21:23 UTC · Python · 38 ms · 16.4 MB

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return ((jewels_set := set(jewels)), len(list(filter(lambda stone: stone in jewels_set, stones))))[-1]
