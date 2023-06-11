// Minimum Interval to Include Each Query
// https://leetcode.com/problems/minimum-interval-to-include-each-query/
// Accepted 2023-06-11 22:16 UTC · C++ · 719 ms · 150.1 MB

class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        int n = intervals.size(), m = queries.size();
        vector<int> output(m, -1);
        
        enum { Start, Query, End };
        vector<tuple<int, int, int>> events;
        for (int i = 0; i < n; ++i) {
            events.push_back(make_tuple(intervals[i][0], Start, i));
            events.push_back(make_tuple(intervals[i][1], End, i));
        }
        for (int i = 0; i < m; ++i) {
            events.push_back(make_tuple(queries[i], Query, i));
        }
        sort(events.begin(), events.end());
        
        multiset<int> sweep_line;
        for (auto &[pos, type, idx] : events) {
            if (type == Query) {
                output[idx] = !sweep_line.empty() ? *sweep_line.begin() : -1;
                continue;
            }
            
            int gap = intervals[idx][1] - intervals[idx][0] + 1;
            if (type == Start) {
                sweep_line.emplace(gap);
            } else {
                auto it = sweep_line.lower_bound(gap);
                sweep_line.erase(it);
            }
        }
        return output;
    }
};
