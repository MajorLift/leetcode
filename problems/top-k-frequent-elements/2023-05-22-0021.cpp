// Top K Frequent Elements
// https://leetcode.com/problems/top-k-frequent-elements/
// Accepted 2023-05-22 00:21 UTC · C++ · 20 ms · 13.6 MB

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        for (int num : nums) {
            map[num]++;
        }
        vector<int> output;
        priority_queue<pair<int, int>> pq;
        for (auto it = map.begin(); it != map.end(); ++it) {
            pq.push(make_pair(it->second, it->first));
            if (pq.size() > map.size() - k) {
                output.push_back(pq.top().second);
                pq.pop();
            }
        }
        return output;
    }
};
