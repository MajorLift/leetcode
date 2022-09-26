# Maximum Units on a Truck
# https://leetcode.com/problems/maximum-units-on-a-truck/
# Accepted 2022-09-26 17:41 UTC · Python · 362 ms · 14.5 MB

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        pq = []
        for [numBoxes, numUnits] in boxTypes:
            heappush(pq, (-numUnits, numBoxes))
        boxesTotal, unitsTotal = truckSize, 0
        while pq and boxesTotal > 0:
            units, boxes = heappop(pq)
            units *= -1
            putOnTruck = boxes if boxesTotal > boxes else boxesTotal
            boxesTotal -= putOnTruck
            unitsTotal += putOnTruck * units
        return unitsTotal
