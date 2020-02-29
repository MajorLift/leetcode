// Max Consecutive Ones
// https://leetcode.com/problems/max-consecutive-ones/
// Accepted 2020-02-29 14:16 UTC · C · 36 ms · 7.2 MB



int findMaxConsecutiveOnes(int* nums, int numsSize){
    int max = 0;
    int curr = 0;
    int i = -1;
    while(++i < numsSize){
        if(nums[i] == 1) curr++;
        else curr = 0;
        if(curr >= max) max = curr;
    }
    return max;
}
