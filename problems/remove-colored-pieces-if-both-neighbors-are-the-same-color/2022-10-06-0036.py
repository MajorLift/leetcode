# Remove Colored Pieces if Both Neighbors are the Same Color
# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
# Accepted 2022-10-06 00:36 UTC · Python · 786 ms · 17.7 MB

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        moves_a, moves_b = [max(len(seg) - 2, 0) for seg in colors.split("B")], [max(len(seg) - 2, 0) for seg in colors.split("A")]
        return sum(moves_a) > sum(moves_b)
