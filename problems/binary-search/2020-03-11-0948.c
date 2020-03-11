// Binary Search
// https://leetcode.com/problems/binary-search/
// Accepted 2020-03-11 09:48 UTC · C · 32 ms · 6.6 MB



int search(int* nums, int numsSize, int target){
    int curr = numsSize / 2;
    int left = 0;
    int right = numsSize - 1;
    while(right - left >= 0 && left >= 0 && right < numsSize){
        if(nums[curr] == target) return curr;
        if(nums[curr] > target) right = curr - 1;
        if(nums[curr] < target) left = curr + 1;
        curr = left + (right - left + 1) / 2;
    }
    return -1;
}
