# Meeting Rooms III
# https://leetcode.com/problems/meeting-rooms-iii/
# Accepted 2023-01-24 18:46 UTC · Python · 2925 ms · 60.4 MB

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        cnt = [0 for i in range(n)]
        rooms = []
        empty = [i for i in range(n)]
        for start, end in meetings:
            while rooms and rooms[0][0] <= start:
                room_end, room_id = heappop(rooms)
                heappush(empty, room_id)
            if empty:
                empty_id = heappop(empty)
                heappush(rooms, (end, empty_id))
                cnt[empty_id] += 1
            else:
                room_end, room_id = heappop(rooms)
                heappush(rooms, (room_end + end - start, room_id))
                cnt[room_id] += 1
        return cnt.index(max(cnt))
