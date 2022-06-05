# Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/
# Accepted 2022-06-05 06:43 UTC · Python · 169 ms · 17.6 MB

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        free_rooms = []
        intervals.sort(key = lambda x: x[0])
        
        heapq.heappush(free_rooms, intervals[0][1])
        for [start, end] in intervals[1:]:
            if free_rooms[0] <= start:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, end)
        
        return len(free_rooms)
