# Meeting Rooms III
# https://leetcode.com/problems/meeting-rooms-iii/
# Accepted 2023-01-24 18:51 UTC · Python · 2027 ms · 60.3 MB

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        cnt = [0 for i in range(n)]
        max_cnt, max_idx = -math.inf, -1
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
                if max_cnt < cnt[empty_id]:
                    max_cnt, max_idx = cnt[empty_id], empty_id
                elif max_cnt == cnt[empty_id] and max_idx > empty_id:
                    max_idx = empty_id
            else:
                room_end, room_id = heappop(rooms)
                heappush(rooms, (room_end + end - start, room_id))
                cnt[room_id] += 1
                if max_cnt < cnt[room_id]:
                    max_cnt, max_idx = cnt[room_id], room_id
                elif max_cnt == cnt[room_id] and max_idx > room_id:
                    max_idx = room_id
        return max_idx
