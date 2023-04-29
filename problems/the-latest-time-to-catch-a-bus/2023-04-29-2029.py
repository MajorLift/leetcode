# The Latest Time to Catch a Bus
# https://leetcode.com/problems/the-latest-time-to-catch-a-bus/
# Accepted 2023-04-29 20:29 UTC · Python · 725 ms · 36.4 MB

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses, passengers = map(sorted, (buses, passengers))
        idx = avail = 0
        for time in buses:
            avail = capacity
            while idx < len(passengers) and avail > 0 and passengers[idx] <= time:
                idx += 1
                avail -= 1
        slot = buses[-1] if avail > 0 else passengers[idx - 1]
        while slot in set(passengers[:idx + 1]):
            slot -= 1
        return slot
