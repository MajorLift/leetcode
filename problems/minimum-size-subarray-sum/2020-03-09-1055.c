// Minimum Size Subarray Sum
// https://leetcode.com/problems/minimum-size-subarray-sum/
// Accepted 2020-03-09 10:55 UTC · C · 8 ms · 6.8 MB

int minSubArrayLen(int s, int* nums, int numsSize){
    int ans = numsSize + 1;
    int sum = 0;
    int left = 0;
    int right = 0;
    while(right < numsSize){
        sum += nums[right];
        while(sum >= s){
            if(right - left + 1 < ans) ans = right - left + 1;
            sum -= nums[left++];
        }
        right++;
    }
    if(ans > numsSize) return 0;
    return ans;
}


// int minSubArrayLen(int s, int* nums, int numsSize){
//     int ans = numsSize + 1;
//     int sum = 0;
//     int left = 0;
//     int right = 0;
//     while(right < numsSize){
//         sum += nums[right];
//         while(sum >= s){
//             int currlen = right - left + 1;
//             if(currlen < ans) ans = currlen;
//             sum -= nums[left++];
//         }
//         right++;
//     }
//     if(ans > numsSize) return 0;
//     return ans;
// }

// int minSubArrayLen(int s, int* nums, int numsSize){
//     int* sums = (int*) malloc(sizeof(int) * (numsSize + 1));
//     sums[0] = 0;
//     int i = 0;
//     while(++i < numsSize + 1) sums[i] = sums[i - 1] + nums[i - 1];
    
// }
