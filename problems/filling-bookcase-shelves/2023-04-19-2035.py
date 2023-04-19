# Filling Bookcase Shelves
# https://leetcode.com/problems/filling-bookcase-shelves/
# Accepted 2023-04-19 20:35 UTC · Python · 56 ms · 15.8 MB

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        widths, heights = map(list, zip(*books))
        @cache
        def dp(i, local_max_h, local_w):
            if local_w > shelfWidth: return +inf
            if i == len(books): return local_max_h
            return min(
                dp(i + 1, max(local_max_h, heights[i]), local_w + widths[i]),  # add to current shelf
                local_max_h + dp(i + 1, heights[i], widths[i]),  # create new shelf
            )
        return dp(0, 0, 0)
