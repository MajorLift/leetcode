# Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/
# Accepted 2022-11-16 01:11 UTC · Python · 52 ms · 13.9 MB

from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        pq = [(-freq, word) for word,freq in cnt.items()]
        heapq.heapify(pq)
        output = []
        while pq and len(output) < k:
            output.append(heapq.heappop(pq)[1])
        return output
