# Minimum Interval to Include Each Query
# https://leetcode.com/problems/minimum-interval-to-include-each-query/
# Accepted 2023-06-11 02:16 UTC · Python · 1904 ms · 63.3 MB

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n, m = map(len, (intervals, queries))
        intervals.sort(key=lambda x: x[1] - x[0] + 1)
        
        output = [-1] * m
        roots = list(range(m + 1))    
        def find(x):
            if roots[x] != x:
                roots[x] = find(roots[x])
            return roots[x]
        
        queries_ord = sorted(queries)
        for a, b in intervals:
            l, r = bisect_left(queries_ord, a), bisect_right(queries_ord, b)
            v = l
            while (v := find(v)) < r:
                output[v] = b - a + 1
                roots[v] += 1
        
        d = {e: i for i,e in enumerate(queries_ord)}
        return [output[d[q]] for q in queries]
