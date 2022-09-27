# High Five
# https://leetcode.com/problems/high-five/
# Accepted 2022-09-27 14:36 UTC · Python · 176 ms · 14.3 MB

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hashmap = defaultdict(list)
        for _id, score in items:
            heappush(hashmap[_id], -score)
        output = []
        for _id, heap in sorted(list(hashmap.items())):
            topFiveSum = 0
            for i in range(5):
                topFiveSum += heappop(heap)
            output.append([_id, int(-topFiveSum / 5)])
        return output
