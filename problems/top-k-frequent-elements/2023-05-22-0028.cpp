// Top K Frequent Elements
// https://leetcode.com/problems/top-k-frequent-elements/
// Accepted 2023-05-22 00:28 UTC · C++ · 18 ms · 13.5 MB

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;
        for (const int& num : nums) {
            cnt[num]++;
        }
        vector<pair<int, int>> p;
        for (auto it = cnt.begin(); it != cnt.end(); ++it) {
            p.emplace_back(-(it->second), it->first);
        }
        nth_element(p.begin(), p.begin() + k - 1, p.end());
        vector<int> output;
        for (int i = 0; i < k; ++i) {
            output.emplace_back(p[i].second);
        }
        return output;
    }
};
