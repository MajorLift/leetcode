# Word Search
# https://leetcode.com/problems/word-search/
# Accepted 2022-12-21 22:29 UTC · Python · 7745 ms · 13.9 MB

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        k = len(word)
        
        def backtrack(path: set[tuple[int, int]], curr: tuple[int, int], idx: int) -> bool:
            if idx == k - 1:
                return True
            x, y = curr
            path.add(curr)
            for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if not (0 <= i < m and 0 <= j < n) or board[i][j] != word[idx + 1] or (i, j) in path:
                    continue
                if backtrack(path, (i, j), idx + 1):
                    return True
            path.remove(curr)
            return False

        return any([backtrack(set(), start, 0) for start in \
            [(i, j) for i in range(m) for j in range(n) if board[i][j] == word[0]]])
