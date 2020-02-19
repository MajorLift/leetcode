// Largest Number At Least Twice of Others
// https://leetcode.com/problems/largest-number-at-least-twice-of-others/
// Accepted 2020-02-19 06:47 UTC · C · 0 ms · 6.8 MB

int* slicecopy(int* nums, int i, int j){
    int* ret = (int*) malloc(sizeof(int) * (j - i));
    int m = 0;
    int n = i;
    while(m < j - i){
        ret[m++] = nums[n++];
    }
    return ret;
}

int findmaxidx(int* nums, int numsSize){
    int curr = nums[0];
    int idx = 0;
    for(int i = 0; i < numsSize; i++){
        if(nums[i] > curr){
            curr = nums[i];
            idx = i;
        }
    }
    return idx;
}

int dominantIndex(int* nums, int numsSize){
    int maxidx = findmaxidx(nums, numsSize);
    int maxval = nums[maxidx];
    int* twicenums = (int*) malloc(sizeof(int) * (numsSize - 1));
    int i = 0;
    while(i < numsSize){
        if(i != maxidx){
            if(2 * nums[i] > maxval) return -1;
        }
        i++;
    }
    return maxidx;
}
