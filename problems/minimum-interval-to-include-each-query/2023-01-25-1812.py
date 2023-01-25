# Minimum Interval to Include Each Query
# https://leetcode.com/problems/minimum-interval-to-include-each-query/
# Accepted 2023-01-25 18:12 UTC · Python · 2584 ms · 52.9 MB

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(reverse=True)
        output = defaultdict(int)
        pq = []
        for query in sorted(queries):
            while intervals and intervals[-1][0] <= query:
                l, r = intervals.pop()
                if r >= query:
                    heappush(pq, (r - l + 1, r))
            while pq and pq[0][1] < query:
                heappop(pq)
            output[query] = pq[0][0] if pq else -1
        return [output[query] for query in queries]
