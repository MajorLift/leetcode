# Least Number of Unique Integers after K Removals
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
# Accepted 2023-01-26 07:29 UTC · Python · 465 ms · 30.9 MB

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr)
        pq = [v for v in cnt.values()]
        heapify(pq)
        while pq and k > 0:
            count = heappop(pq)
            k -= count
        return len(pq) + (0 if k >= 0 else 1)
