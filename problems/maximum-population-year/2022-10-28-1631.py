# Maximum Population Year
# https://leetcode.com/problems/maximum-population-year/
# Accepted 2022-10-28 16:31 UTC · Python · 85 ms · 14 MB

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        updates = []
        for birth, death in logs:
            updates.append((birth, +1))
            updates.append((death, -1))
        updates.sort()
        
        population = max_pop = max_year = 0
        for year, diff in updates:
            population += diff
            if population > max_pop:
                max_pop = population
                max_year = year
        return max_year
