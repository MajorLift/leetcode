// Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/
// Accepted 2023-09-11 17:39 UTC · C++ · 132 ms · 73.4 MB

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        return set(nums.begin(), nums.end()).size() < nums.size();
    }
};
