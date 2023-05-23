// Permutations
// https://leetcode.com/problems/permutations/
// Accepted 2023-05-23 01:36 UTC · C++ · 2 ms · 7.9 MB

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        _n = nums.size();
        _nums = nums;
        backtrack(0);
        return output;
    }
private:
    vector<int> _nums;
    vector<vector<int>> output;
    int _n;
    void backtrack(int start) {
        if (start == _n - 1) {
            output.push_back(_nums);
            return;
        }
        for (int i = start; i < _n; ++i) {
            swap(_nums[start], _nums[i]);
            backtrack(start + 1);
            swap(_nums[start], _nums[i]);
        }
    }
};
