// Minimum Interval to Include Each Query
// https://leetcode.com/problems/minimum-interval-to-include-each-query/
// Accepted 2023-06-11 01:27 UTC · C++ · 681 ms · 150 MB

class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        int n = intervals.size(), m = queries.size();
        vector<int> output(m, -1);

        enum { Start, Query, End } PointType;
        vector<tuple<int, int, int>> events;
        for (int i = 0; i < n; ++i) {
            events.push_back({Start, intervals[i][0], i});
            events.push_back({End, intervals[i][1], i});
        }
        for (int i = 0; i < m; ++i) {
            events.push_back({Query, queries[i], i});
        }

        sort(events.begin(), events.end(), [&](const tuple<int, int, int>& a, const tuple<int, int, int>& b) {
            if (get<1>(a) == get<1>(b)) return get<0>(a) < get<0>(b);
            return get<1>(a) < get<1>(b);
        });

        multiset<int> sweep_line;
        for (auto &[type, pos, idx] : events) {
            if (type == Start) {
                sweep_line.emplace(intervals[idx][1] - intervals[idx][0] + 1);
            } else if (type == End) {
                auto it = sweep_line.lower_bound(intervals[idx][1] - intervals[idx][0] + 1);
                sweep_line.erase(it);
            } else {
                output[idx] = sweep_line.begin() == sweep_line.end() ? -1 : *sweep_line.begin();
            }
        }
        return output;
    }
};
