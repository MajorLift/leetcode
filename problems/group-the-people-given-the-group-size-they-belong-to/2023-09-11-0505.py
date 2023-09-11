# Group the People Given the Group Size They Belong To
# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
# Accepted 2023-09-11 05:05 UTC · Python · 79 ms · 16.4 MB

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        output, groups = [], defaultdict(list)
        for i,e in enumerate(groupSizes):
            groups[e].append(i)
        return [members[size * i : size * (i + 1)] 
            for size, members in groups.items() 
            for i in range(len(members) // size)]
