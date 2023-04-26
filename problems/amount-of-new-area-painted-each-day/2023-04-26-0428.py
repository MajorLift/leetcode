# Amount of New Area Painted Each Day
# https://leetcode.com/problems/amount-of-new-area-painted-each-day/
# Accepted 2023-04-26 04:28 UTC · Python · 2770 ms · 69.5 MB

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        n = len(paint)
        records = []
        maxr = 0
        for i, (start, end) in enumerate(paint):
            records.append((start, i, 'START'))
            records.append((end, i, 'END'))
            maxr = max(maxr, end)
        records.sort()
        
        ans, pq, visited = [0] * n, [], set()
        i = 0
        for pos in range(maxr + 1):
            while i < len(records) and records[i][0] == pos:
                pos, idx, _type = records[i]
                if _type == 'START':
                    heappush(pq, idx)
                if _type == 'END':
                    visited.add(idx)
                i += 1

            while pq and pq[0] in visited:
                heappop(pq)

            if pq:
                ans[pq[0]] += 1
                
        return ans
