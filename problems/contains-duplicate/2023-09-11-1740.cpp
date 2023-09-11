// Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/
// Accepted 2023-09-11 17:40 UTC · C++ · 122 ms · 71.8 MB

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> mp;
        for (auto num : nums) mp[num]++;
        for (auto pair : mp) {
            if (pair.second > 1) return true;
        }
        return false;
    }
};
