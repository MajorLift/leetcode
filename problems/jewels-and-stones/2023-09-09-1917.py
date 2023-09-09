# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/
# Accepted 2023-09-09 19:17 UTC · Python · 47 ms · 16.3 MB

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len(re.findall(f'[{jewels}]', stones))
