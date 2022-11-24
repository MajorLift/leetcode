// Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/
// Accepted 2022-11-24 06:21 UTC · C++ · 271 ms · 46.6 MB

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] == nums[i + 1]) return true;
        }
        return false;
    }
};
