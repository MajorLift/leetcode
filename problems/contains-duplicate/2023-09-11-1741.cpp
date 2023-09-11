// Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/
// Accepted 2023-09-11 17:41 UTC · C++ · 74 ms · 57.2 MB

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] == nums[i - 1]) return true;
        }
        return false;
    }
};
