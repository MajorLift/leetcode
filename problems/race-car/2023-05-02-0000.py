# Race Car
# https://leetcode.com/problems/race-car/
# Accepted 2023-05-02 00:00 UTC · Python · 81 ms · 16.7 MB

class Solution:
    def racecar(self, target: int) -> int:
        pq = [(0, 0, 1)]
        while pq:
            moves, pos, speed = heappop(pq)
            if pos == target:
                return moves
            heappush(pq, (moves + 1, pos + speed, speed * 2))
            if speed > 0 and pos + speed > target \
                or speed < 0 and pos + speed < target:
                heappush(pq, (moves + 1, pos, -1 if speed > 0 else 1))
        return -1
