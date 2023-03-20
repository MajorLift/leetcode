# Gas Station
# https://leetcode.com/problems/gas-station/
# Accepted 2023-03-20 22:33 UTC · Python · 1070 ms · 19.9 MB

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total = tank = start = 0
        for i in range(n):
            total += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start if total >= 0 else -1
