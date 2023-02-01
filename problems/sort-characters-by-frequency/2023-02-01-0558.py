# Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/
# Accepted 2023-02-01 05:58 UTC · Python · 40 ms · 15.3 MB

class Solution:
    def frequencySort(self, s: str) -> str:
        freqs = sorted(list(Counter(s).items()), key=lambda x: x[1])[::-1]
        return "".join(k * v for k, v in freqs)
