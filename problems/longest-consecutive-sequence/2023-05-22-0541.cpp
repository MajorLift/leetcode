// Longest Consecutive Sequence
// https://leetcode.com/problems/longest-consecutive-sequence/
// Accepted 2023-05-22 05:41 UTC · C++ · 213 ms · 75.1 MB

class UnionFind {
private:
    typedef vector<int> vi;
    vi root;
    vi groupSize;
    int _maxGroupSize;
public:
    UnionFind(int n) {
        for (int i = 0; i < n; ++i) {
            root.push_back(i);
            groupSize.push_back(1);
            _maxGroupSize = 1;
        }
    }

    int find(int x) {
        if (x == root[x]) return x;
        root[x] = find(root[x]);
        return root[x];
    }

    void merge(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX == rootY) return;
        root[rootY] = rootX;
        groupSize[rootX] += groupSize[rootY];
        _maxGroupSize = max(_maxGroupSize, groupSize[rootX]);
    }

    int maxGroupSize() {
        return _maxGroupSize;
    }
};

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        unordered_map<int, int> map;
        int serial = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (!map.count(nums[i])) {
                map[nums[i]] = serial++;
            }
        }
        UnionFind uf = UnionFind(map.size());
        for (auto& [k, v] : map) {
            if (map.count(k - 1)) uf.merge(v, map[k - 1]);
        }
        return uf.maxGroupSize();
    }
};
