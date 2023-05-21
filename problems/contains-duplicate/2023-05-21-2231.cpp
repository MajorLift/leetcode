// Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/
// Accepted 2023-05-21 22:31 UTC · C++ · 180 ms · 71.6 MB

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> mp;
        for (auto i : nums) mp[i]++;
        for (auto i : mp) {
            if (i.second >= 2) return true;
        }
        return false;
    }
};
