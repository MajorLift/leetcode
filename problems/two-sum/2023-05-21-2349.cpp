// Two Sum
// https://leetcode.com/problems/two-sum/
// Accepted 2023-05-21 23:49 UTC · C++ · 12 ms · 10.9 MB

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;
        for (int i = 0; i < nums.size(); ++i) {
            if (mp.find(target - nums[i]) != mp.end()) {
                return {mp[target - nums[i]], i};
            }
            mp[nums[i]] = i;
        }
        return {};
    }
};
