// Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/
// Accepted 2023-05-21 22:46 UTC · C++ · 214 ms · 73.4 MB

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        return nums.size() > set<int>(nums.begin(), nums.end()).size();
    }
};
