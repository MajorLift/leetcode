// Minimum Interval to Include Each Query
// https://leetcode.com/problems/minimum-interval-to-include-each-query/
// Accepted 2023-06-11 21:40 UTC · C++ · 762 ms · 121.9 MB

class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        int n = intervals.size(), m = queries.size();
        vector<int> output(m, -1);

        deque<pair<int, int>> intervals_deq(n);
        for (int i = 0; i < n; ++i) {
            intervals_deq.push_back(make_pair(intervals[i][0], intervals[i][1]));
        }
        sort(intervals_deq.begin(), intervals_deq.end());

        vector<pair<int, int>> query_enum(m);
        for (int i = 0; i < m; ++i) {
            query_enum.push_back(make_pair(queries[i], i));
        }
        sort(query_enum.begin(), query_enum.end());

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        for (auto &[query, query_idx] : query_enum) {
            while (!intervals_deq.empty() && intervals_deq.front().first <= query) {
                auto &[l, r] = intervals_deq.front();
                pq.emplace(make_pair(r - l + 1, r));
                intervals_deq.pop_front();
            }
            while (!pq.empty() && pq.top().second < query) {
                pq.pop();
            }
            output[query_idx] = !pq.empty() 
                ? pq.top().first 
                : -1;
        }
        return output;
    }
};
