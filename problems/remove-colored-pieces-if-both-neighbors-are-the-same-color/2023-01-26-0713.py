# Remove Colored Pieces if Both Neighbors are the Same Color
# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
# Accepted 2023-01-26 07:13 UTC · Python · 175 ms · 17.6 MB

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        def total_score(player):
            return sum(max(len(seg) - 2, 0) \
                for seg in colors.split("A" if player == "B" else "B") \
                if seg)
        return total_score("A") > total_score("B")
