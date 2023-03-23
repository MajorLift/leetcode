# Partition Labels
# https://leetcode.com/problems/partition-labels/
# Accepted 2023-03-23 02:02 UTC · Python · 51 ms · 14 MB

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        charmap = defaultdict(list)
        for i, char in enumerate(s):
            if len(charmap[char]) < 2:
                charmap[char].append(i)
            else:
                charmap[char][1] = i
        charmap = {k: v for k, v in charmap.items() if len(v) > 1}

        output = [[]]
        for i, char in enumerate(s):
            if not output[-1]:
                output[-1].append(i)
                if char not in charmap:
                    output[-1].append(i + 1)
                    output.append([])
                else:
                    output[-1].append(charmap[char][1] + 1)
            else:
                if i == output[-1][1] - 1:
                    output.append([])
                elif char in charmap:
                    output[-1][1] = max(output[-1][1], charmap[char][1] + 1)
        if not output[-1]:
            output.pop()
        return [e[1] - e[0] for e in output]
