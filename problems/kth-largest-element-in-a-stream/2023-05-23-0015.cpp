// Kth Largest Element in a Stream
// https://leetcode.com/problems/kth-largest-element-in-a-stream/
// Accepted 2023-05-23 00:15 UTC · C++ · 41 ms · 19.9 MB

class KthLargest {
private:
    int _k;
    priority_queue<int> pq;
public:
    KthLargest(int k, vector<int>& nums) {
        _k = k;
        for (const int& num : nums) add(num);
    }
    
    int add(int val) {
        pq.push(-val);
        while (pq.size() > _k) pq.pop();
        return -pq.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
