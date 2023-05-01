# Shortest Way to Form String
# https://leetcode.com/problems/shortest-way-to-form-string/
# Accepted 2023-05-01 02:56 UTC · Python · 47 ms · 16.3 MB

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        n, m = map(len, (source, target))
        if set(target) - set(source):
            return -1
        
        invertidx = defaultdict(list)
        for i, char in enumerate(source):
            invertidx[char].append(i)
        
        cnt = 1
        prev = -1
        for char in target:
            idxs = invertidx[char]
            curr = bisect_left(idxs, prev + 1)
            if curr < len(idxs):
                prev = idxs[curr]
            else:
                prev = idxs[0]
                cnt += 1
        return cnt
