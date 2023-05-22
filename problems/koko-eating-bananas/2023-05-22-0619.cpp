// Koko Eating Bananas
// https://leetcode.com/problems/koko-eating-bananas/
// Accepted 2023-05-22 06:19 UTC · C++ · 48 ms · 18.9 MB

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int lo = 1, hi = *(max_element(piles.begin(), piles.end()));
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (eatingTime(piles, mid) > h) lo = mid + 1;
            else hi = mid;
        }
        return hi;
    }
private:
    int eatingTime(vector<int>& piles, int k) {
        long long ans = 0;
        for (int& pile : piles) {
            ans += ceil(pile / (double) k);
        }
        return ans;
    }
};
