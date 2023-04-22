# Meeting Rooms III
# https://leetcode.com/problems/meeting-rooms-iii/
# Accepted 2023-04-22 02:50 UTC · Python · 1465 ms · 60.3 MB

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        avail = list(range(n))
        used = []
        cnt = [0] * n
        for start, end in sorted(meetings, key=lambda x: x[0]):
            while used and used[0][0] <= start:
                heappush(avail, heappop(used)[1])
            if avail:
                room = heappop(avail)
                heappush(used, (end, room))
            else:
                next_end, room = heappop(used)
                heappush(used, (next_end + (end - start), room))
            cnt[room] += 1
        return cnt.index(max(cnt))
