# Maximum Subsequence Score
# https://leetcode.com/problems/maximum-subsequence-score/
# Accepted 2023-05-24 19:44 UTC · Python · 981 ms · 38.5 MB

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        pairs = list(zip(nums1, nums2))
        pairs.sort(key=lambda x: -x[1])
        pq = [x[0] for x in pairs[:k]]
        top_k_sum = sum(pq)
        heapify(pq)
        global_max = top_k_sum * pairs[k - 1][1]
        for i in range(k, n):
            top_k_sum += -heappushpop(pq, pairs[i][0]) + pairs[i][0]
            global_max = max(global_max, top_k_sum * pairs[i][1])
        return global_max
