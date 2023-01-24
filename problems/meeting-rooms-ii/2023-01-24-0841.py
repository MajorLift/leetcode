# Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/
# Accepted 2023-01-24 08:41 UTC · Python · 141 ms · 17.5 MB

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        rooms = [intervals[0][1]]
        ans = 1
        for start, end in intervals[1:]:
            if rooms[0] <= start:
                heapreplace(rooms, end)
            else:
                heappush(rooms, end)
                ans += 1
        return ans
