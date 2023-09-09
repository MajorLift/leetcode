# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/
# Accepted 2023-09-09 18:52 UTC · Python · 52 ms · 16.4 MB

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len(re.compile(f'[{jewels}]').findall(stones))
