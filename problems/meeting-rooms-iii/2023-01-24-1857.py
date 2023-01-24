# Meeting Rooms III
# https://leetcode.com/problems/meeting-rooms-iii/
# Accepted 2023-01-24 18:57 UTC · Python · 4418 ms · 60.4 MB

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        rooms = []
        empty = [(i, 0) for i in range(n)]
        for start, end in meetings:
            while rooms and rooms[0][0] <= start:
                room_end, room_id, room_cnt = heappop(rooms)
                heappush(empty, (room_id, room_cnt))
            if empty:
                empty_id, empty_cnt = heappop(empty)
                heappush(rooms, (end, empty_id, empty_cnt + 1))
            else:
                room_end, room_id, room_cnt = heappop(rooms)
                heappush(rooms, (room_end + (end - start), room_id, room_cnt + 1))
        return sorted([(room_id, room_cnt) \
            for _, room_id, room_cnt in rooms] + empty, \
            key=lambda x: (-x[1], x[0]))[0][0]
