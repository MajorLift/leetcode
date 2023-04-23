# The Latest Time to Catch a Bus
# https://leetcode.com/problems/the-latest-time-to-catch-a-bus/
# Accepted 2023-04-23 01:26 UTC · Python · 730 ms · 33.6 MB

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses, passengers = map(sorted, (buses, passengers))
        idx = avail = 0
        for time in buses:
            avail = capacity
            while idx < len(passengers) \
                and avail > 0 \
                and passengers[idx] <= time:
                idx += 1
                avail -= 1
        slot = buses[-1] if avail > 0 else passengers[idx - 1]
        while slot in set(passengers):
            slot -= 1
        return slot
