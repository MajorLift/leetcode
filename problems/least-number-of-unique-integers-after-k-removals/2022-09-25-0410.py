# Least Number of Unique Integers after K Removals
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
# Accepted 2022-09-25 04:10 UTC · Python · 1603 ms · 35 MB

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freqs = defaultdict(int)
        for num in arr:
            freqs[num] += 1
            
        pq = []
        for num, freq in freqs.items():
            heappush(pq, (freq, num))
        while k > 0:
            curr_freq, curr_num = heappop(pq)
            if curr_freq > 1:
                curr_freq -= 1
                heappush(pq, (curr_freq, curr_num))
            k -= 1
        return len(pq)
