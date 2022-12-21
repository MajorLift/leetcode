# Word Search
# https://leetcode.com/problems/word-search/
# Accepted 2022-12-21 23:54 UTC · Python · 31 ms · 14 MB

from collections import Counter, defaultdict

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        word_cnt, char_coords = Counter(word), defaultdict(set)
        [char_coords[board[i][j]].add((i, j)) for i in range(m) for j in range(n) \
            if board[i][j] in word_cnt]
        
        if len(word_cnt) != len(char_coords) or \
            not all([word_cnt[k] <= len(char_coords[k]) for k in word_cnt]):
            return False

        if len(char_coords[word[-1]]) < len(char_coords[word[0]]):
            word = word[::-1]
        
        def backtrack(coord, idx):
            if idx == len(word) - 1:
                return True
            x, y = coord
            char_coords[word[idx]].remove(coord)
            for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                if (i, j) not in char_coords[word[idx + 1]]:
                    continue
                if backtrack((i, j), idx + 1):
                    return True
            char_coords[word[idx]].add(coord)
            return False

        for i, j in [*char_coords[word[0]]]:
            if backtrack((i, j), 0):
                return True
        return False
