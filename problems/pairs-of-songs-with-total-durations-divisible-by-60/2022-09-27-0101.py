# Pairs of Songs With Total Durations Divisible by 60
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
# Accepted 2022-09-27 01:01 UTC · Python · 306 ms · 17.7 MB

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = defaultdict(int)
        count = 0
        for t in time:
            count += remainders[(60 - t) % 60]
            remainders[t % 60] += 1
        return count
