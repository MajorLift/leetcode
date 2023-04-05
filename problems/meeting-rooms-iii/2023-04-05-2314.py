# Meeting Rooms III
# https://leetcode.com/problems/meeting-rooms-iii/
# Accepted 2023-04-05 23:14 UTC · Python · 1419 ms · 60.3 MB

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        busy, idle, cnt = [], [i for i in range(n)], [0 for i in range(n)]
        for start, end in sorted(meetings, key=lambda x: x[0]):
            while busy and busy[0][0] <= start:
                room_end, room_id = heappop(busy)
                heappush(idle, room_id)
            if idle:
                room_id = heappop(idle)
                heappush(busy, (end, room_id))
            else:
                room_end, room_id = heappop(busy)
                heappush(busy, (room_end + end - start, room_id))
            cnt[room_id] += 1
        return cnt.index(max(cnt))
