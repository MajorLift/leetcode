# Shortest Way to Form String
# https://leetcode.com/problems/shortest-way-to-form-string/
# Accepted 2023-05-02 01:57 UTC · Python · 36 ms · 16.2 MB

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        m, n = map(len, (source, target))
        sourceIdxMap = defaultdict(list)
        for i, char in enumerate(source):
            sourceIdxMap[char].append(i)

        cnt = 1
        prev = -1
        for char in target:
            if char not in sourceIdxMap:
                return -1
            idxs = sourceIdxMap[char]
            curr = bisect_left(idxs, prev + 1)
            if curr == len(idxs):
                prev = idxs[0]
                cnt += 1
            else:
                prev = idxs[curr]
        return cnt
