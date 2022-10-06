# Remove Colored Pieces if Both Neighbors are the Same Color
# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
# Accepted 2022-10-06 00:37 UTC · Python · 520 ms · 17.9 MB

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        moves_a, moves_b = [max(len(seg) - 2, 0) for seg in colors.split("B") if seg], [max(len(seg) - 2, 0) for seg in colors.split("A") if seg]
        return sum(moves_a) > sum(moves_b)
