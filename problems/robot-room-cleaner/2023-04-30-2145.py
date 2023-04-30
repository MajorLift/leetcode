# Robot Room Cleaner
# https://leetcode.com/problems/robot-room-cleaner/
# Accepted 2023-04-30 21:45 UTC · Python · 76 ms · 17.8 MB

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def revert():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))
        visited = set()
        def backtrack(curr, d):
            visited.add(curr)
            robot.clean()
            for i in range(4):
                new_d = (d + i) % 4
                r, c = map(sum, zip(DIRECTIONS[new_d], curr))
                if (r, c) not in visited and robot.move():
                    backtrack((r, c), new_d)
                    revert()
                robot.turnRight()
        
        backtrack((0, 0), 0)
