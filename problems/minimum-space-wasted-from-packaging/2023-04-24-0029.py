# Minimum Space Wasted From Packaging
# https://leetcode.com/problems/minimum-space-wasted-from-packaging/
# Accepted 2023-04-24 00:29 UTC · Python · 1477 ms · 38.5 MB

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n, m = len(packages), len(boxes)
        packages, boxes = sorted(packages), [sorted(b) for b in boxes]
        if packages[-1] > max(b[-1] for b in boxes):
            return -1

        global_min = +inf
        for catalogue in boxes:
            if catalogue[-1] < packages[-1]:
                continue
            total = prev = curr = 0
            for size in catalogue:
                curr = bisect_right(packages, size)
                total += (curr - prev) * size
                prev = curr
            global_min = min(global_min, total)
        return (global_min - sum(packages)) % MOD
