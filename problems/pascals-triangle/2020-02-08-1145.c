// Pascal's Triangle
// https://leetcode.com/problems/pascals-triangle/
// Accepted 2020-02-08 11:45 UTC · C · 4 ms · 7.3 MB



/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */


void recursive_pascal(int **q, int numRows, int i, int** returnColumnSizes){    
    if(i >= numRows){
        return;
    }
    q[i] = (int*) malloc(sizeof(int) * (i+1));
    q[i][0] = 1;
    q[i][i] = 1;
    
    *(*returnColumnSizes + i) = i+1;
    
    int j = 1;
    while(j < i){
        q[i][j] = q[i-1][j-1] + q[i-1][j];
        j += 1;
    }
        
    recursive_pascal(q, numRows, i+1, returnColumnSizes);
}


int** generate(int numRows, int* returnSize, int** returnColumnSizes){
    *returnSize = numRows;
    int** q = (int**) malloc(sizeof(int*) * numRows);        
    *returnColumnSizes = (int*) malloc(sizeof(int) * numRows);
    recursive_pascal(q, numRows, 0, returnColumnSizes);
    return q;
}
