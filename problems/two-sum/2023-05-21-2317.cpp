// Two Sum
// https://leetcode.com/problems/two-sum/
// Accepted 2023-05-21 23:17 UTC · C++ · 400 ms · 10 MB

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size() - 1; ++i) {
            for (int j = i + 1; j < nums.size(); ++j) {
                if (nums[i] + nums[j] == target) return {i, j};
            }
        }
        return {};
    }
};
