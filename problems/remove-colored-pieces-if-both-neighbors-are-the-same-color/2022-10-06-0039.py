# Remove Colored Pieces if Both Neighbors are the Same Color
# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
# Accepted 2022-10-06 00:39 UTC · Python · 181 ms · 17.9 MB

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        return sum([max(len(seg) - 2, 0) for seg in colors.split("B") if seg]) > sum([max(len(seg) - 2, 0) for seg in colors.split("A") if seg])
