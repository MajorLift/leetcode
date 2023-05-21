// Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/
// Accepted 2023-05-21 22:45 UTC · C++ · 134 ms · 57.2 MB

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 1; ++i) {
            if (nums[i] == nums[i + 1]) return true;
        }
        return false;
    }
};
