// Unique Paths
// https://leetcode.com/problems/unique-paths/
// Accepted 2021-11-02 23:57 UTC · JavaScript · 76 ms · 39.4 MB

/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    const memo = [];
    for (let i = 0; i < m; i += 1) {
        const row = [];
        for (let j = 0; j < n; j += 1) {
            row.push(0);
        }
        memo.push(row);
    }
    
    // top-down tabulation
    // for (let i = m - 1; i >= 0; i -= 1) {
    //     for (let j = n - 1; j >= 0; j -= 1) {
    //         if (i === m - 1 || j === n - 1) memo[i][j] = 1;
    //         else memo[i][j] = memo[i + 1][j] + memo[i][j + 1];
    //     }
    // }
    // return memo[0][0];
    
    // bottom-up memoization
    for (let i = 0; i < m; i += 1) {
        for (let j = 0; j < n; j += 1) {
            if (i === 0 || j === 0) memo[i][j] = 1;
            else memo[i][j] = memo[i - 1][j] + memo[i][j - 1];
        }
    }
    return memo[m - 1][n - 1];
};
