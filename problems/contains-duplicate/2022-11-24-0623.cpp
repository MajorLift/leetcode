// Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/
// Accepted 2022-11-24 06:23 UTC · C++ · 159 ms · 54.6 MB

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int,int> mp;
        for(auto i : nums) mp[i]++;
        for(auto i : mp) {
            if(i.second >= 2) return true;
        }
        return false;
    }
};
