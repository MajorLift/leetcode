// Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/
// Accepted 2023-09-11 17:38 UTC · C++ · 103 ms · 71.8 MB

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> mp;
        for (auto i : nums) mp[i]++;
        for (auto i : mp) {
            if (i.second > 1) return true;
        }
        return false;
    }
};
