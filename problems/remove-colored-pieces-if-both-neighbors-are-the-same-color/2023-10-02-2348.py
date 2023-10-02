# Remove Colored Pieces if Both Neighbors are the Same Color
# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
# Accepted 2023-10-02 23:48 UTC · Python · 142 ms (91.28%) · 19.7 MB (5.29%)

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        def total_score(player):
            return sum(max(len(seg) - 2, 0) \
                for seg in colors.split(("A", "B")[player == "A"]) \
                if seg)
        return total_score("A") > total_score("B")
