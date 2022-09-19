# Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/
# Accepted 2022-09-19 02:00 UTC · Python · 120 ms · 15.4 MB

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0 for _ in range(numCourses)]
        adj_list = [[] for _ in range(numCourses)]
        for [course, prereq] in prerequisites:
            indegrees[course] += 1
            adj_list[prereq].append(course)
        
        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
        output = []
        while queue:
            curr = queue.popleft()
            output.append(curr)
            for course in adj_list[curr]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    queue.append(course)
        return output if all([x == 0 for x in indegrees]) else []
