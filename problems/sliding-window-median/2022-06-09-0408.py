# Sliding Window Median
# https://leetcode.com/problems/sliding-window-median/
# Accepted 2022-06-09 04:08 UTC · Python · 128 ms · 16.3 MB

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        medians = []
        
        # initialize heap with k elems
        lo, hi = [], []
        for i in range(k):
            heapq.heappush(lo, -nums[i])
        for j in range(k // 2):
            heapq.heappush(hi, -heapq.heappop(lo))
        medians.append(-lo[0] if k % 2 > 0 else (-lo[0] + hi[0]) / 2)
        
        invalidated = {num: 0 for num in nums}
        # iterate over remainder of nums and populate medians
        for head_idx in range(k, len(nums)):     
            balance = 0
            in_num, out_num = nums[head_idx], nums[head_idx - k]
            # print(in_num, out_num)
            
            # exit
            if out_num <= -lo[0]:
                balance -= 1
            else:
                balance += 1
            invalidated[out_num] += 1
                
            # enter
            if len(lo) > 0 and in_num <= -lo[0]:
                heapq.heappush(lo, -in_num)
                balance += 1
            else:
                heapq.heappush(hi, in_num)
                balance -= 1
            
            # balance
            if balance < 0:
                heapq.heappush(lo, -heapq.heappop(hi))
                balance += 1
            if balance > 0:
                heapq.heappush(hi, -heapq.heappop(lo))
                balance -= 1
            # print(balance)
            
            # removed
            while invalidated[-lo[0]] > 0:
                invalidated[-lo[0]] -= 1
                heapq.heappop(lo)
            while len(hi) > 0 and invalidated[hi[0]] > 0:
                invalidated[hi[0]] -= 1
                heapq.heappop(hi)
            # print(invalidated)
            
            medians.append(-lo[0] if k % 2 > 0 else (-lo[0] + hi[0]) / 2)
            # print(lo, hi)
            
        return medians
