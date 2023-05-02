# Meeting Rooms III
# https://leetcode.com/problems/meeting-rooms-iii/
# Accepted 2023-05-02 16:12 UTC · Python · 1488 ms · 62.8 MB

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        idle, busy, cnt = list(range(n)), [], [0] * n

        for start, end in sorted(meetings, key=lambda x:x[0]):
            while busy and busy[0][0] <= start:
                heappush(idle, heappop(busy)[1])

            if idle:
                room_id = heappop(idle)
                heappush(busy, (end, room_id))
            
            elif busy:
                nxt_end, room_id = heappop(busy)
                heappush(busy, (nxt_end + (end - start), room_id))
            
            cnt[room_id] += 1

        return cnt.index(max(cnt))
