// Minimum Size Subarray Sum
// https://leetcode.com/problems/minimum-size-subarray-sum/
// Accepted 2020-02-29 21:50 UTC · C · 4 ms · 6.9 MB


int minSubArrayLen(int s, int* nums, int numsSize){
    int ans = numsSize + 1;
    int sum = 0;
    int left = 0;
    int right = 0;
    while(right < numsSize){
        sum += nums[right];
        while(sum >= s){
            int currlen = right - left + 1;
            if(currlen < ans) ans = currlen;
            sum -= nums[left++];
        }
        right++;
    }
    if(ans > numsSize) return 0;
    return ans;
}
