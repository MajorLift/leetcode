# N-Queens II
# https://leetcode.com/problems/n-queens-ii/
# Accepted 2022-06-03 04:25 UTC · Python · 680 ms · 13.8 MB

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.output = 0
        
        def backtrack(curr = (0, 0), 
                      count = 0, 
                      stack = [(x, y) for x in range(n) for y in range(n)]):
            i, j = curr
            if count == n:
                self.output += 1
                
            new_stack = []
            for x, y in stack:
                if x != i and y != j and abs((x - i) / (y - j)) != 1:
                    new_stack.append((x, y))

            while(len(new_stack)):
                backtrack(new_stack.pop(), count + 1, new_stack)
        
        for i in range(n):
            backtrack((0, i), 1)

        return self.output
