# Filling Bookcase Shelves
# https://leetcode.com/problems/filling-bookcase-shelves/
# Accepted 2023-04-19 20:28 UTC · Python · 59 ms · 15.9 MB

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        widths, heights = map(list, zip(*books))
        @cache
        def dp(i, height, width):
            if width > shelfWidth: 
                return +inf
            if i >= len(books):
                return height
            return min(dp(i + 1, max(height, heights[i]), width + widths[i]), 
                height + dp(i + 1, heights[i], widths[i]))
        return dp(0, 0, 0)
