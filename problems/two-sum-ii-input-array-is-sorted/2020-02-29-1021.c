// Two Sum II - Input Array Is Sorted
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
// Accepted 2020-02-29 10:21 UTC · C · 4 ms · 6.5 MB



/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){
    int i, j;
    *returnSize = 2;
    int* ret = (int*) malloc(sizeof(int) * (*returnSize));
    
    if(numbers[0] >= 0){
        i = 0;
        while(++i < numbersSize && numbers[i] <= target);
    }
    else i = numbersSize;
    while(--i > 0){
        j = -1;
        while(++j < i){
            if(numbers[j] + numbers[i] == target) break;
        }
        if(j < i) break;
    }
    
    ret[0] = j + 1;
    ret[1] = i + 1;
    return ret;
}
