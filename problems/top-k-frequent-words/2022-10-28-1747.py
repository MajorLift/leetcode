# Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/
# Accepted 2022-10-28 17:47 UTC · Python · 133 ms · 13.9 MB

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = Counter(words)
        maxheap = [(-count, word) for word, count in freqs.items()]
        heapq.heapify(maxheap)
        output = []
        for _ in range(k):
            _, word = heapq.heappop(maxheap)
            output.append(word)
        return output
