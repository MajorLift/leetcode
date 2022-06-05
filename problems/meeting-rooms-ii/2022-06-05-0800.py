# Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/
# Accepted 2022-06-05 08:00 UTC · Python · 153 ms · 17.7 MB

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([e[0] for e in intervals])
        ends = sorted([e[1] for e in intervals])
        
        result = 0
        e_ptr = 0
        for start in starts:
            if start < ends[e_ptr]:
                result += 1
            else:
                e_ptr += 1
        
        return result
