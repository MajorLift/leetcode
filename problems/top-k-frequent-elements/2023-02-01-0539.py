# Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# Accepted 2023-02-01 05:39 UTC · Python · 102 ms · 18.7 MB

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pairs = sorted(list(Counter(nums).items()), key=lambda x: -x[1])[:k]
        return [pair[0] for pair in pairs]
