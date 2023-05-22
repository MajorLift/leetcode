// Longest Consecutive Sequence
// https://leetcode.com/problems/longest-consecutive-sequence/
// Accepted 2023-05-22 05:47 UTC · C++ · 187 ms · 67.1 MB

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n = nums.size();
        unordered_set<int> set;
        for (int& num : nums) {
            set.insert(num);
        }
        int global_max = 0;
        for (int& num : nums) {
            if (!set.count(num + 1)) {
                int curr = num;
                int local_max = 1;
                while (set.count(curr - 1)) {
                    curr--;
                    local_max++;
                }
                global_max = max(global_max, local_max);
            }
        }
        return global_max;
    }
};
