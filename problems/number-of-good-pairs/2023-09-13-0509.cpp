// Number of Good Pairs
// https://leetcode.com/problems/number-of-good-pairs/
// Accepted 2023-09-13 05:09 UTC · C++ · 3 ms (41.54%) · 7.4 MB (8.63%)

class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int ans = 0;
        unordered_map<int, int> freq;
        for (auto& num : nums) {
            if (freq.contains(num)) ans += freq[num]++;
            else freq.emplace(make_pair(num, 1));
        }
        return ans;
    }
};
