// Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/
// Accepted 2022-11-24 06:22 UTC · C++ · 163 ms · 54.6 MB

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        return nums.size() > set<int>(nums.begin(),nums.end()).size();
    }
};
