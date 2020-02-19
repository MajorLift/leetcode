// Find Pivot Index
// https://leetcode.com/problems/find-pivot-index/
// Accepted 2020-02-19 06:16 UTC · C · 16 ms · 7.8 MB



int pivotIndex(int* nums, int numsSize){
    int sum_all = 0;
    int i = 0;
    while(i < numsSize){
        sum_all += nums[i++];
    }
    int sum_left = 0;
    int sum_right = 0;
    i = 0;
    while(i < numsSize){
        if(i > 0) sum_left += nums[i - 1];
        sum_right = sum_all - (sum_left + nums[i]);
        if(sum_left == sum_right) return i;
        i++;
    }
    return -1;
}
