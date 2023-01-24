# Find Servers That Handled Most Number of Requests
# https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/
# Accepted 2023-01-24 21:02 UTC · Python · 2514 ms · 35.3 MB

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        cnt = defaultdict(int)
        busy = []
        available = [_id for _id in range(k)]
        for i, (start, duration) in enumerate(zip(arrival, load)):
            while busy and start >= busy[0][0]:
                server_end, server_id = heappop(busy)
                insort(available, server_id)
            if not available:
                continue
            idx = bisect_left(available, i % k)
            assigned_id = available[idx] if idx < len(available) else available[0]
            available.remove(assigned_id)            
            cnt[assigned_id] += 1
            heappush(busy, (start + duration, assigned_id))
        max_count = max(cnt.values())
        return [k for k, v in cnt.items() if v == max_count]
