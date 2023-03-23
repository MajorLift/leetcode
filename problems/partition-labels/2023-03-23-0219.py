# Partition Labels
# https://leetcode.com/problems/partition-labels/
# Accepted 2023-03-23 02:19 UTC · Python · 38 ms · 13.8 MB

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charmap = {}
        for i, char in enumerate(s):
            charmap[char] = i

        output = []
        size = last = 0
        for i, char in enumerate(s):
            size += 1
            last = max(last, charmap[char])
            if i == last:
                output.append(size)
                size = 0
        return output
