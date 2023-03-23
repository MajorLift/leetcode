# Partition Labels
# https://leetcode.com/problems/partition-labels/
# Accepted 2023-03-23 02:16 UTC · Python · 45 ms · 13.9 MB

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        charmap = defaultdict(list)
        for i, char in enumerate(s):
            if len(charmap[char]) < 2:
                charmap[char].append(i)
            else:
                charmap[char][1] = i
        charmap = {k: v[1] for k, v in charmap.items() if len(v) > 1}

        output = []
        size = last = 0
        for i, char in enumerate(s):
            size += 1
            last = max(last, charmap.get(char, i))
            if i == last:
                output.append(size)
                size = last = 0
        return output
