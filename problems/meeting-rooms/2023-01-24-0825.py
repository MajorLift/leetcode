# Meeting Rooms
# https://leetcode.com/problems/meeting-rooms/
# Accepted 2023-01-24 08:25 UTC · Python · 128 ms · 17.6 MB

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: (x[0], x[1]))
        for i in range(len(intervals) - 1):
            curr_start, curr_end = intervals[i]
            next_start, next_end = intervals[i + 1]
            if curr_start <= next_start < curr_end:
                return False
        return True
