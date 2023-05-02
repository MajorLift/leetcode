# Max Points on a Line
# https://leetcode.com/problems/max-points-on-a-line/
# Accepted 2023-05-02 23:09 UTC · Python · 159 ms · 42.2 MB

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2: 
            return len(points)

        hashmap = defaultdict(lambda: defaultdict(set))
        for (x1, y1), (x2, y2) in combinations(points, 2):
            if x1 == x2: 
                a, b = +inf, x1
            elif y1 == y2: 
                a, b = 0, y1
            else: 
                a = (y1 - y2) / (x1 - x2)
                b = y1 - a * x1
            # print(a, b, (x1, y1), (x2, y2))
            hashmap[a][b].add((x1, y1))
            hashmap[a][b].add((x2, y2))
        # print(hashmap)
        return max(len(vb) for va in hashmap.values() for vb in va.values())
