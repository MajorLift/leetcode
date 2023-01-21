# Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Accepted 2023-01-21 04:48 UTC · Python · 164 ms · 18.8 MB

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for word in strs:
            output[str(sorted(Counter(word).items()))].append(word)
        return output.values()
