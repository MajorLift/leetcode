// Minimum Interval to Include Each Query
// https://leetcode.com/problems/minimum-interval-to-include-each-query/
// Accepted 2023-06-11 01:41 UTC · C++ · 590 ms · 114 MB

class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        int n = intervals.size(), m = queries.size();
        vector<int> output(m, -1);

        vector<pair<int, int>> query_enum(m);
        for (int i = 0; i < m; ++i) {
            query_enum.push_back(make_pair(queries[i], i));
        }
        sort(intervals.begin(), intervals.end());
        sort(query_enum.begin(), query_enum.end());

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        int idx = 0;
        for (auto &[query, query_idx] : query_enum) {
            for (; idx < n && intervals[idx][0] <= query; ++idx) {
                pq.push({intervals[idx][1] - intervals[idx][0] + 1, idx});
            }
            while (!pq.empty() && intervals[pq.top().second][1] < query) pq.pop();
            output[query_idx] = pq.empty() ? -1 : pq.top().first;
        }
        return output;
    }
};
