# The Latest Time to Catch a Bus
# https://leetcode.com/problems/the-latest-time-to-catch-a-bus/
# Accepted 2023-05-02 16:42 UTC · Python · 720 ms · 37.1 MB

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()

        idx, avail = 0, +inf
        for time in buses:
            avail = capacity
            while idx < len(passengers) \
                and avail > 0 \
                and passengers[idx] <= time:
                avail -= 1
                idx += 1
        
        slot = buses[-1]
        if avail == 0:
            slot = passengers[idx - 1]
        while slot in set(passengers):
            slot -= 1
        return slot
