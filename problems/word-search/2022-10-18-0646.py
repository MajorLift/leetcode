# Word Search
# https://leetcode.com/problems/word-search/
# Accepted 2022-10-18 06:46 UTC · Python · 7925 ms · 14.1 MB

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        k = len(word)
        m, n = len(board), len(board[0])

        def backtrack(path, curr):
            x, y = curr
            if len(path) == k:
                return True
            for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= i < m and 0 <= j < n \
                    and (i, j) not in path \
                    and board[i][j] == word[len(path)]:
                    path.add((i, j))
                    if backtrack(path, (i, j)):
                        return True
                    path.remove((i, j))
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(set([(i, j)]), (i, j)):
                        return True
        return False
