# Minimum Space Wasted From Packaging
# https://leetcode.com/problems/minimum-space-wasted-from-packaging/
# Accepted 2023-05-02 01:41 UTC · Python · 1468 ms · 40.8 MB

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n, m = map(len, (packages, boxes))
        pkg_sum = sum(packages)
        packages.sort()
        suppliers = [sorted(catalogue) for catalogue in boxes]
        global_min = +inf
        for catalogue in suppliers:
            if catalogue[-1] < packages[-1]:
                continue
            total = currIdx = prevIdx = 0
            for box in catalogue:
                currIdx = bisect_right(packages, box)
                total += (currIdx - prevIdx) * box
                prevIdx = currIdx
            global_min = min(global_min, total - pkg_sum)
        return global_min % MOD if global_min < +inf else -1
