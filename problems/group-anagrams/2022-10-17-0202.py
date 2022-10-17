# Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Accepted 2022-10-17 02:02 UTC · Python · 351 ms · 20.4 MB

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        freqs = [defaultdict(int) for _ in range(n)]
        freqs_map = defaultdict(list)
        for i in range(n):
            for char in strs[i]:
                freqs[i][char] += 1
            freqs_map[str(sorted(freqs[i].items()))].append(strs[i])
        return freqs_map.values()
