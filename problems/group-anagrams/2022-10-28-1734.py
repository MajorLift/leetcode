# Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Accepted 2022-10-28 17:34 UTC · Python · 411 ms · 18.4 MB

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        groups = defaultdict(list)
        for s in strs:
            freqs = [0] * 26
            for char in s:
                freqs[ord(char.lower()) - ord('a')] += 1
            groups["#".join([str(num) for num in freqs])].append(s)
        return groups.values()
