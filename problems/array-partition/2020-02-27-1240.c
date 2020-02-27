// Array Partition
// https://leetcode.com/problems/array-partition/
// Accepted 2020-02-27 12:40 UTC · C · 56 ms · 9.8 MB

#include <stdlib.h>

// void sortArray(int* nums, int numsSize){
    
// }

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}


int arrayPairSum(int* nums, int numsSize){
    // sortArray(nums, numsSize);
    qsort(nums, numsSize, sizeof(int), compare);
    int ret = 0;
    int i = -1;
    while(++i < numsSize / 2) ret += nums[2 * i];
    return ret;
}
