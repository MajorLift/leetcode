# Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Accepted 2022-10-19 22:28 UTC · Python · 1215 ms · 27.1 MB

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for num in nums:
            if len(minheap) < k:
                heapq.heappush(minheap, num)
            else:
                heapq.heappushpop(minheap, num)
        return minheap[0]
