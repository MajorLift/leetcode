# Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/
# Accepted 2022-06-09 04:47 UTC · Python · 132 ms · 17.5 MB

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
    
        intervals = sorted(intervals, key=lambda x: x[0])
        # print(intervals)
        
        # min_heap of ending times only
        end_times = [intervals[0][1]]
        counter = 1
        
        # iterate over intervals list and compare start_time to top of min_heap
        for [start, end] in intervals[1:]:
            # if start_time is earlier than top, need new room 
            # increment counter and push end_time of curr meeting into min_heap
            # without! popping min_heap since top meeting is still ongoing
            if start < end_times[0]:
                counter += 1
                heapq.heappush(end_times, end)
            # else, no need for new room, pop min_heap, push end_time of curr meeting
            else:
                heapq.heapreplace(end_times, end)
            # print(end_times)
            
        return counter
