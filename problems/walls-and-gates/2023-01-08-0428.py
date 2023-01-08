# Walls and Gates
# https://leetcode.com/problems/walls-and-gates/
# Accepted 2023-01-08 04:28 UTC · Python · 262 ms · 16.9 MB

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        m, n = len(rooms), len(rooms[0])
        queue = collections.deque([(i, j) for i, j in itertools.product(range(m), range(n)) if rooms[i][j] == 0])
        while queue:
            r, c = queue.popleft()
            for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= i < m and 0 <= j < n and rooms[r][c] + 1 < rooms[i][j]:
                    rooms[i][j] = rooms[r][c] + 1
                    queue.append((i, j))
