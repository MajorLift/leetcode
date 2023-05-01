# Check if Word Can Be Placed In Crossword
# https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/
# Accepted 2023-05-01 19:10 UTC · Python · 1887 ms · 37.7 MB

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n, k = map(len, (board, board[0], word))
        EMPTY, BLOCKED = ' ', '#'
        return any(len(s) == k 
                    and all(s[i] == w[i] or s[i] == EMPTY
                            for i in range(k)) 
            for row in board + list(zip(*board))
            for s in ''.join(row).split('#')
            for w in (word, word[::-1]))
