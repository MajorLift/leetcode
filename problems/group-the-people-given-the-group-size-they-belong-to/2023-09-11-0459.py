# Group the People Given the Group Size They Belong To
# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
# Accepted 2023-09-11 04:59 UTC · Python · 77 ms · 16.5 MB

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        output, groups = [], defaultdict(list)
        for i,e in enumerate(groupSizes):
            groups[e].append(i)
        for size, members in groups.items():
            while members:
                output.append(members[:size])
                members = members[size:]
        return output
